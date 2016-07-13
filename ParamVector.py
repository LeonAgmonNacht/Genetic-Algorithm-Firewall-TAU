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

    def __init__(self):
        """
        init self with empty data
        """
        self.ip_src_set = set()
        self.ip_dst_set = set()
        self.src_port_set = set()
        self.dst_port_set = set()
        self.sizes_set_low_bound = 0
        self.sizes_set_high_bound = 0
        self.ttl_thresh = 0
        self.protocol_set = set()
        self.seq_num_low_bound = 0
        self.seq_num_high_bound = 0
        self.weight_of = {}

    @staticmethod
    def generate_random_data():
        """
        creates a ParamVector with random data
        :return: an instance of ParamVector that is defined using random data
        """
        pass