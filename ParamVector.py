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

    # random data constants:

    SIZE_RANDOM_LOW_MIN = 0
    SIZE_RANDOM_LOW_MAX = 2000
    SIZE_RANDOM_HIGH_MIN = 1
    SIZE_RANDOM_HIGH_MAX = 2000
    TTL_THRESH_MIN = 0
    TTL_THRESH_MAX = 255
    SEQ_TRESH_MIN = 0
    SEQ_THRESH_MAX = 2**31
    WEIGHT_MAX_VAL = 10

    # the functions that can be used to mutate a ParamVector, instances of ProbabilityFunction
    mutate_functions = []

    def __init__(self, ip_src_set=set(), ip_dst_set=set(), port_src_set=set(), port_dst_set=set(),
                 sizes_low_bound=0, sizes_high_bound=0, ttl_thresh=0, protocol_set=set(),
                 seq_low_bound=0, seq_high_bound=0, weight_of={}):
        """
        init self with all the needed variables
        :param ip_src_set: a set of tuples (with 4 ints) representing the source ip addresses.
        :param ip_dst_set: a set of tuples (with 4 ints) representing the destination ip addresses.
        :param src_port_set: a set of ints representing the source port addresses.
        :param dst_port_set: a set of ints representing the destination port addresses.
        :param sizes_low_bound: a number that is the low bound for the sizes
        :param sizes_high_bound: a number that is the high bound for the sizes
        :param ttl_thresh: a number that is the thresh hold for the TTL(time to live)
        :param protocol_set: a set of strings representing the protocols
        :param seq_low_bound: a number that is the low bound for the sequence number
        :param seq_high_bound: a number that is the high bound for the sequence number
        :param weight_of: a dictionary that takes the name of a variable and returns the weight of it in the fitness
        """
        self.ip_src_set = ip_src_set
        self.ip_dst_set = ip_dst_set
        self.port_src_set = port_src_set
        self.port_dst_set = port_dst_set
        self.sizes_low_bound = sizes_low_bound
        self.sizes_high_bound = sizes_high_bound
        self.ttl_thresh = ttl_thresh
        self.protocol_set = protocol_set
        self.seq_low_bound = seq_low_bound
        self.seq_high_bound = seq_high_bound
        self.weight_of = weight_of

    def mutate(self):
        """
        applying the mutate mechanism on self
        :return: a new ParamVector instance with the mutated data in self
        """
        pass
    
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
        size_low = randint(SIZE_RANDOM_LOW_MIN, SIZE_RANDOM_LOW_MAX)
        size_high = size_low + randint(SIZE_RANDOM_HIGH_MIN, SIZE_RANDOM_HIGH_MAX)
        ttl = randint(TTL_THRESH_MIN, TTL_THRESH_MAX)
        protoc = get_random_protocol()
        seq_low = randint(SEQ_TRESH_MIN, SEQ_TRESH_MAX)
        seq_high = seq_low + randint(SEQ_TRESH_MIN, SEQ_TRESH_MAX)

        weights = {DST_IP : uniform(0, WEIGHT_MAX_VAL),
                   SRC_IP : uniform(0, WEIGHT_MAX_VAL),
                   DST_PORT : uniform(0, WEIGHT_MAX_VAL),
                   SRC_PORT : uniform(0, WEIGHT_MAX_VAL),
                   SIZE : uniform(0, WEIGHT_MAX_VAL),
                   TTL : uniform(0, WEIGHT_MAX_VAL),
                   PROTOCOL : uniform(0, WEIGHT_MAX_VAL),
                   SEQ : uniform(0, WEIGHT_MAX_VAL)}

        sum_weights = sum(weights.values())

        # normalizing the values:

        for key in weights.keys():
            weights[key] = weights[key]/sum_weights

        return ParamVector(ip_src_set=set(src_ip),
                           ip_dst_set=set(dst_ip),
                           port_src_set=set(src_port),
                           port_dst_set=set(dst_port),
                           sizes_low_bound=size_low,
                           sizes_high_bound=size_high,
                           ttl_thresh=ttl,
                           protocol_set=set(protoc),
                           seq_low_bound=seq_low,
                           seq_high_bound=seq_high,
                           weight_of=weights)


    def __add__(self, other):
        result = None
        #do_shit
        result.mutate()
        return result

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
        repr += "sizes_low" + suffix + str(self.sizes_low_bound) + "::"
        repr += "sizes_high" + suffix + str(self.sizes_high_bound) + "::"
        repr += "ttl" + suffix + str(self.ttl_thresh) + "::"
        repr += "protocol" + suffix + str(self.protocol_set) + "::"
        repr += "seq_low" + suffix + str(self.seq_low_bound) + "::"
        repr += "seq_high" + suffix + str(self.seq_high_bound) + "::"
        repr += "weight" + suffix + str(self.weight_of)
        return repr
