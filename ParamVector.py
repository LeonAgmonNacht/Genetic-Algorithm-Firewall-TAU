from random import randint, uniform
from MemoizationUtils import get_random_protocol

class ParamVector(object):
    """
    This class represents the vectors that defines a firewall
    a ParamVector is a class that represents a vector that defines a firewall.
    we have our indicator functions that should get parameters, lets call these functions g1...gn
    for each gi we can say that there is a vector (ai1,...,aim) of scalars. so we can represent every firewall Fl
    as the sum of wi*gi  where wi(weight) is a scalar.
    so we can think about a vector of different sized vectors, where every vector i is:
    fi, ai1,...aim
    :ivar weight_of: weight_of contains the following keys: DST_IP, SRC_IP, DST_PORT, SRC_PORT, SIZE, TTL, PROTOCOL, SEQ
    """

    # constants:

    DST_IP = "dstIP"
    SRC_IP = "srcIP"
    DST_PORT = "dstPort"
    SRC_PORT = "srcPort"
    SIZE = "size"
    TTL = "ttl"
    PROTOCOL = "protocol"
    SEQ = "seq_number"
    weight_keys = {DST_IP, SRC_IP, DST_PORT,
                   SRC_PORT,
                   SIZE,
                   TTL,
                   PROTOCOL,
                   SEQ}

    # random data constants:

    SIZE_RANDOM_LOW_MIN = 0
    SIZE_RANDOM_LOW_MAX = 2000
    SIZE_RANDOM_HIGH_MIN = 1
    SIZE_RANDOM_HIGH_MAX = 2000
    TTL_THRESH_MIN = 0
    TTL_THRESH_MAX = 255
    SEQ_THRESH_MIN = 0
    SEQ_THRESH_MAX = 2**31
    WEIGHT_MAX_VAL = 10

    # the functions that can be used to mutate a ParamVector, instances of ProbabilityFunction
    mutate_functions = []

    def __init__(self, ip_src_set=set(), ip_dst_set=set(), port_src_set=set(), port_dst_set=set(),
                 sizes_lower_bound=0, sizes_upper_bound=0, ttl_lower_bound=0, protocol_set=set(),
                 seq_lower_bound=0, seq_upper_bound=0, weight_of={key: 0 for key in weight_keys}):
        """
        init self with all the needed variables
        :param ip_src_set: a set of tuples (with 4 ints) representing the source ip addresses.
        :param ip_dst_set: a set of tuples (with 4 ints) representing the destination ip addresses.
        :param src_port_set: a set of ints representing the source port addresses.
        :param dst_port_set: a set of ints representing the destination port addresses.
        :param sizes_lower_bound: a number that is the low bound for the sizes
        :param sizes_upper_bound: a number that is the high bound for the sizes
        :param ttl_lower_bound: a number that is the thresh hold for the TTL(time to live)
        :param protocol_set: a set of strings representing the protocols
        :param seq_lower_bound: a number that is the low bound for the sequence number
        :param seq_upper_bound: a number that is the high bound for the sequence number
        :param weight_of: a dictionary that takes the name of a variable and returns the weight of it in the fitness
        """
        self.ip_src_set = ip_src_set
        self.ip_dst_set = ip_dst_set
        self.port_src_set = port_src_set
        self.port_dst_set = port_dst_set
        self.sizes_lower_bound = sizes_lower_bound
        self.sizes_upper_bound = sizes_upper_bound
        self.ttl_lower_bound = ttl_lower_bound
        self.protocol_set = protocol_set
        self.seq_lower_bound = seq_lower_bound
        self.seq_upper_bound = seq_upper_bound
        self.weight_of = weight_of

    def mutate(self):
        """
        applying the mutate mechanism on self
        :return: a new ParamVector instance with the mutated data in self
        """
        return self

    @staticmethod
    def generate_random_data():
        """
        creates a ParamVector with random data
        :return: an instance of ParamVector that is defined using random data
        """
        # helper lambdas:
        random_ip = lambda: tuple([randint(0, 255) for _ in range(4)])
        random_port = lambda: randint(0, 65535)

        src_ip = random_ip()
        dst_ip = random_ip()
        src_port = random_port()
        dst_port = random_port()
        size_low = randint(ParamVector.SIZE_RANDOM_LOW_MIN, ParamVector.SIZE_RANDOM_LOW_MAX)
        size_high = size_low + randint(ParamVector.SIZE_RANDOM_HIGH_MIN, ParamVector.SIZE_RANDOM_HIGH_MAX)
        ttl = randint(ParamVector.TTL_THRESH_MIN, ParamVector.TTL_THRESH_MAX)
        protoc = get_random_protocol()
        seq_low = randint(ParamVector.SEQ_THRESH_MIN, ParamVector.SEQ_THRESH_MAX)
        seq_high = seq_low + randint(ParamVector.SEQ_THRESH_MIN, ParamVector.SEQ_THRESH_MAX)

        weight_func = lambda: uniform(0, ParamVector.WEIGHT_MAX_VAL)

        weights = {ParamVector.DST_IP : weight_func(),
                   ParamVector.SRC_IP : weight_func(),
                   ParamVector.DST_PORT : weight_func(),
                   ParamVector.SRC_PORT : weight_func(),
                   ParamVector.SIZE : weight_func(),
                   ParamVector.TTL : weight_func(),
                   ParamVector.PROTOCOL : weight_func(),
                   ParamVector.SEQ : weight_func()}

        sum_weights = sum(weights.values())

        # normalizing the values:

        for key in weights.keys():
            weights[key] = weights[key]/sum_weights

        return ParamVector(ip_src_set={src_ip},
                           ip_dst_set={dst_ip},
                           port_src_set={src_port},
                           port_dst_set={dst_port},
                           sizes_lower_bound=size_low,
                           sizes_upper_bound=size_high,
                           ttl_lower_bound=ttl,
                           protocol_set={protoc},
                           seq_lower_bound=seq_low,
                           seq_upper_bound=seq_high,
                           weight_of=weights)

    @staticmethod
    def _mate_ordinals(*ordinals):
        """
        mates two ordinal sets representations
        :param ordinals: the ordinals
        :return: one of the given ordinal sets or their union.
        """
        return {0:ordinals[0],1:ordinals[1],2:ordinals[0].union(ordinals[1])}[randint(0,2)]

    @staticmethod
    def _mate_bounds(is_max,*bounds):
        # TODO: add docs
        return {0: bounds[0], 1: bounds[1], 2: sum(bounds)}[randint(0, 2)]

    def __add__(self, other):
        """
        creates a mate between these ParamVectors
        :param other: another ParamVector
        :return: a "child" of the given ParamVectors
        """
        assert isinstance(other, ParamVector)
        weights = {}
        for param in self.weight_keys:
            if randint(0,1):
                weights[param] = self[param]
            else:
                weights[param] = other[param]

        result = ParamVector(ParamVector._mate_ordinals(self.ip_src_set, other.ip_src_set),
                                  ParamVector._mate_ordinals(self.ip_dst_set, other.ip_dst_set),
                                  ParamVector._mate_ordinals(self.port_dst_set, other.port_dst_set),
                                  ParamVector._mate_ordinals(self.port_src_set, other.port_src_set),
                                  ParamVector._mate_bounds(False, self.sizes_lower_bound, other.sizes_lower_bound),
                                  ParamVector._mate_bounds(True, self.sizes_upper_bound, other.sizes_upper_bound),
                                  ParamVector._mate_bounds(False, self.ttl_lower_bound, other.ttl_lower_bound),
                                  ParamVector._mate_ordinals(self.protocol_set, other.protocol_set),
                                  ParamVector._mate_bounds(False, self.seq_lower_bound, other.seq_lower_bound),
                                  ParamVector._mate_bounds(True, self.seq_upper_bound, other.seq_lower_bound), weights)
        return result.mutate()


    def __getitem__(self, item):
        """
        :param item: name of the field which should be returned
        :return: the value of this field
        """
        # assert item in self.weight_keys
        return self.weight_of[item]

    def __repr__(self):
        """
        :return: a string that represents a ParamVector
        """

        repr = ""
        suffix = ","
        repr += "src_ip" + suffix + str(self.ip_src_set) + "::"
        repr += "dst_ip" + suffix + str(self.ip_dst_set) + "::"
        repr += "src_port" + suffix + str(self.port_src_set) + "::"
        repr += "dst_port" + suffix + str(self.port_dst_set) + "::"
        repr += "sizes_low" + suffix + str(self.sizes_lower_bound) + "::"
        repr += "sizes_high" + suffix + str(self.sizes_upper_bound) + "::"
        repr += "ttl" + suffix + str(self.ttl_lower_bound) + "::"
        repr += "protocol" + suffix + str(self.protocol_set) + "::"
        repr += "seq_low" + suffix + str(self.seq_lower_bound) + "::"
        repr += "seq_high" + suffix + str(self.seq_upper_bound) + "::"
        repr += "weight" + suffix + str(self.weight_of)
        return repr
