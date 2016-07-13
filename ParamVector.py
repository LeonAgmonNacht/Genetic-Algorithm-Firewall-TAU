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
        pass

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
