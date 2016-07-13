import random
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
        pass

    def __add__(self, other):
        """
        creates a mate between these ParamVectors
        :param other: another ParamVector
        :return: a "child" of the given ParamVectors
        """
        assert not isinstance(other, ParamVector)
        weights = {}
        for param in self.weight_keys:
            if(random.randint(0,1)):
                weights[param] = self[param]
        result = ParamVector(ParamVector.mate_ordinals(self.ip_src_set, other.ip_src_set),
                                  ParamVector._mate_ordinals(self.ip_dst_set, other.ip_dst_set),
                                  ParamVector._mate_ordinals(self.port_dst_set, other.port_dst_set),
                                  ParamVector._mate_ordinals(self.port_src_set, other.port_src_set),
                                  ParamVector._mate_bounds(False, self.sizes_lower_bound, other.sizes_lower_bound),
                                  ParamVector._mate_bounds(True, self.sizes_upper_bound, other.sizes_upper_bound),
                                  ParamVector._mate_bounds(False, self.ttl_lower_bound, other.ttl_lower_bound),
                                  ParamVector.mate_ordinals(self.protocol_set, other.protocol_set),
                                  ParamVector(False, self.seq_lower_bound, other.seq_lower_bound),
                                  ParamVector._mate_bounds(True, self.seq_upper_bound, other.seq_lower_bound), weights)
        return result.mutate()

    @staticmethod
    def _mate_ordinals(*ordinals):
        """
        mates two ordinal sets representations
        :param ordinals: the ordinals
        :return: one of the given ordinal sets or their union.
        """
        return {0:ordinals[0],1:ordinals[1],2:sum(ordinals)}[random.randint(0,2)]

    @staticmethod
    def _mate_bounds(is_max,*bounds):
        return {0: bounds[0], 1: bounds[1], 2: sum(bounds)}[random.randint(0, 2)]

    def __getitem__(self, item):
        """
        :param item: name of the field which should be returned
        :return: the value of this field
        """
        assert item not in self.weight_keys
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
