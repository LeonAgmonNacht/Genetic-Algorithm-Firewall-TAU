# Created by Leon Agmon Nacht
from collections import namedtuple
from Function import Function
from PacketDataParser import *

# single data (vector) methods:

particular_data_indicator_tuple = namedtuple("ParticularDataIndicator",
                                             ["ip_method",
                                              "port_method",
                                              "size_packet_method",
                                              "ttl_method",
                                              "type_packet_method",
                                              "sequence_num_method"])

# methods types:
simple_indicator_method = Function(lambda (param, arr): param in arr)
range_indicator_method = Function(lambda (val, min_value, max_val): min_value <= val <= max_val)
greater_indicator_method = Function(lambda (val, threshold): val > threshold)

# structure that contains the needed functions

particular_data_indicator = particular_data_indicator_tuple(ip_method=simple_indicator_method,
                                                            port_method=simple_indicator_method,
                                                            size_packet_method=range_indicator_method,
                                                            ttl_method=greater_indicator_method,
                                                            type_packet_method=simple_indicator_method,
                                                            sequence_num_method=Function(lambda val, min_value, max_val:
                                                            not range_indicator_method(val, min_value, max_val)))

class FireWall(object):
    """
    a class representing a firewall (the ability to detect malicious packets)
    :ivar param_vector: the vector that defines the behaviour of self, an instance of ParamVector
    """

    def __init__(self, param_vector):
        """
        creates a firewall from the given data in param_vector
        :param param_vector: an instance of ParamVector that holds the needed data to define a FireWall instance
        :return: the new created FireWall instance
        """
        # the function that should return if a packet is malicious or not:
        self.func = FireWall.individual_firewall_generator(param_vector)
        self.param_vector = param_vector

    def __call__(self, data_vector):
        return self.func(data_vector)

    @staticmethod
    def individual_firewall_generator(param_vector):
        """
        the method can create firewalls uniquely using the given param_vector
        :param param_vector: an instance of ParamVector that holds the needed data to define a FireWall instance
        :return: a function that returns a value in the range [0,1]. the function recevies a Packet (a row of DataFrame)
        and returns a value where 1 is malicous and 0 is clean
        """
        sum_weights = sum(param_vector.weight_of.values())
        ip_src_func = Function(lambda ip: particular_data_indicator.ip_method(ip, param_vector.ip_src_set))
        ip_dst_func = Function(lambda ip: particular_data_indicator.ip_method(ip, param_vector.ip_dst_set))
        port_src_func = Function(lambda port: particular_data_indicator_tuple.port_method(port, param_vector.port_src_set))
        port_dst_func = Function(lambda port: particular_data_indicator_tuple.port_method(port, param_vector.port_dst_set))
        size_func = Function(lambda size: particular_data_indicator.size_method(size,
                                                                                 param_vector.sizes_lower_bound,
                                                                                 param_vector.sizes_upper_bound))
        ttl_func = Function(lambda ttl: particular_data_indicator.ttl_method(ttl, param_vector.ttl_lower_bound))
        protocol_func = Function(lambda pr: particular_data_indicator.type_packet_method(pr, param_vector.protocol_set))
        seq_func = Function(lambda seq: particular_data_indicator.sequence_num_method(seq,
                                                                                      param_vector.seq_lower_bound,
                                                                                      param_vector.seq_upper_bound))
        all_func = lambda packet:\
            ip_src_func(packet[SRC_IP_STRING])+\
            ip_dst_func(packet[DST_IP_STRING])+\
            port_src_func(packet[SRC_PORT_STRING])+\
            port_dst_func(packet[DST_PORT_STRING])+\
            size_func(packet[SIZE_STRING])+\
            ttl_func(packet[TTL_STRING])+\
            protocol_func(packet[PROTOCOL_STRING])+\
            seq_func(packet[SEQ_NUM_STRING])

        normlized_func = lambda packet: all_func(packet)/sum_weights
        return Function(normlized_func)

    @staticmethod
    def mate_param_vectors(param_vector1, param_vector2):
        """
        in GAs we want to improve the solution every step of the algorithm, in order to do that we use two older
        solutions and then we randomly apply merge between both:
        for every param in the ParamVector of the firewall, we will randomly choose if this param will merge with
        his equivalent in the other individual, or not. If not, we will choose which of the params (the param from
        individual 1 or 2) will remain after the mate. This way some of the params in params will be
        the merge of individual 1 and 2, and some will stay uniq (from individual 1 or 2).
        :param param_vector1: the first ParamVector to merge
        :param param_vector2: the second ParamVector to merge
        :return: a new ParamVector that is the merge of both
        """
        return FireWall.individual_firewall_generator(param_vector1 + param_vector2)

    def is_malicious(self,packet):
        """
        :param packet: the packet in whatever format you would like to use
        :return:
        """
        pass
    
    def __repr__(self):
        """
        The represent of a firewall is just the represent of its ParamVector
        :return: a string representation of the firewall
        """
        return "FireWall-" + str(self.param_vector)