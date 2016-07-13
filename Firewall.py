# Created by Leon Agmon Nacht
from collections import namedtuple
from Function import Function

class FireWall(object):
    """
    a class representing a firewall (the ability to detect malicious packets)
    """
    def __init__(self, param_vector):
        """
        creates a firewall from the given data in param_vector
        :param param_vector: an instance of ParamVector that holds the needed data to define a FireWall instance
        :return: the new created FireWall instance
        """
        # the function that should return if a packet is malicious or not:
        self.func = FireWall.individual_firewall_generator(param_vector)
    def __call__(self, data_vector):
        return self.func(data_vector)
    @staticmethod
    def individual_firewall_generator(param_vector):
        """
        the method can create firewalls uniquely using the given param_vector
        :param param_vector: an instance of ParamVector that holds the needed data to define a FireWall instance
        :return: a new firewall defined entirely by the given data (param_vector)
        """
        # TODO: zemmel asked to implement
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
        pass


# single data (vector) methods:
particular_data_indicator_tuple = namedtuple("ip_method",
                                       "port_method",
                                       "size_packet_method",
                                       "ttl_method",
                                       "type_packet_method",
                                       "sequence_num_method")

# methods types:
simple_indicator_method = Function(lambda (param, arr): param in arr)
range_indicator_method = Function(lambda (val, min_value, max_val): min_value <= val <= max_val)
greater_indicator_method = Function(lambda (val, threshold): val > threshold)

# structure that contains the needed functions

particular_data_indicator = particular_data_indicator_tuple(ip_method=simple_indicator_method,
                                                            port_method=simple_indicator_method,
                                                            size_packet_method=range_indicator_method,
                                                            ttl_method=simple_indicator_method,
                                                            type_packet_method=simple_indicator_method,
                                                            sequence_num_method=lambda val, min_value, max_va:
                                                            not range_indicator_method(val, min_value, max_va))
