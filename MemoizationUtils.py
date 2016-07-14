from ParamVector import *
from Firewall import FireWall
from ast import literal_eval
from random import choice


def get_set_from_string(set_string):
    """
    :param set_string: a string represent of a set
    :return: the set that is being represented
    """
    exec "t = " + set_string
    return t


def get_param_vector_from_string(param_vector_string):
    """
    :param param_vector_string: a string represent of a ParamVector object (has to be in the repr format)
    :return: a ParamVector that is being represented in the string
    """
    param_vector_list = param_vector_string.split("::")
    args = [param_vector_list[i].split(',')[1] for i in range(len(param_vector_list))]
    args[0] = get_set_from_string(args[0])
    args[1] = get_set_from_string(args[1])
    args[2] = get_set_from_string(args[2])
    args[3] = get_set_from_string(args[3])
    args[4] = int(args[4])
    args[5] = int(args[5])
    args[6] = int(args[6])
    args[7] = get_set_from_string(args[7])
    args[8] = int(args[8])
    args[9] = int(args[9])
    args[10] = literal_eval(args[10])
    return ParamVector(*args)


def get_firewall_from_string(firewall_string):
    """
    :param firewall_string: a string represent of a Firewall object (has to be in the repr format)
    :return: a FireWall that is being represented in the string
    """
    return FireWall(get_param_vector_from_string(firewall_string.split("-")[1]))


# protocols:

protocols_file = open("protocols.txt")
protocols_lines = protocols_file.readlines()
protocols = [line.split(" ")[0] for line in protocols_lines]


def get_random_protocol():
    """
    :return: a random string representing a protocol supported by the scapy library
    """
    return choice(protocols)
