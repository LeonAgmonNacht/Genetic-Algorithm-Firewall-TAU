# Created by Leon Agmon Nacht
from collections import namedtuple
from Functions import Function

def individual_firewall_generator(param_vector):
    """
    the method can create firewalls uniquely using the given param_vector
    :param param_vector: an instance of ParamVector that holds the needed data to define a FireWall instance
    :return: a new firewall defined entirely by the given data (param_vector)
    """



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
        self.func = individual_firewall_generator(param_vector)


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
                                                            sequence_num_method=greater_indicator_method)
