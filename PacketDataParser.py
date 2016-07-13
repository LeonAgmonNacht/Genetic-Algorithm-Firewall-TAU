import pandas as pd
from scapy.all import *

# constants:

DST_IP_STRING = "dstIP"
SRC_IP_STRING = "srcIP"
DST_PORT_STRING = "dstPort"
SRC_PORT_STRING = "srcPort"
SIZE_STRING = "size"
TTL_STRING = "ttl"
PROTOCOL_STRING = "protocol"
SEQ_NUM_STRING = "seq"

def get_packets_from_pcap(pcap_path):
    """
    receives the packets from the given file path
    :param pcap_path: the path to the pcap file to load the data from
    :return: list of Packets holding the data in the pcap file
    """
    packets = []  # the packets of the given pcap file
    pcap_data = rdpcap(pcap_path)
    for p in pcap_data:
        packets.append(p)
    return packets


def read_packets(file_path):
    """
    reads the content of the given pcap file into pandas matrix saving only the wanted data, meaning:
    Source IP address
    Destination IP address
    Source port number
    Destination port number
    Size of packet
    Time to Live (TTL)
    Packet type
    Sequence number
    :param file_path: the path to the pcap file to load
    :return: a pandas matrix containing the wanted data in the given pcap file
    """
    packets = get_packets_from_pcap(file_path)
    packets_data = []
    for sc_packet in packets:

        dstIP = sc_packet[IP].dst
        srcIP = sc_packet[IP].src
        dstPort = sc_packet.dport
        srcPort = sc_packet.sport
        size = len(sc_packet)
        ttl = sc_packet.ttl
        seq = sc_packet.seq
        # get upper layer in packet:
        layer_count = 0
        while sc_packet.getlayer(layer_count):
            layer_count += 1

        protocol = sc_packet.getlayer(layer_count - 2).name
        packets_data.append([dstIP, srcIP, dstPort, srcPort, size, ttl, protocol, seq])

    # created pandas dataFrame with found data:
    data = pd.DataFrame(data=packets_data,
                        columns=[DST_IP_STRING,
                                 SRC_IP_STRING,
                                 DST_PORT_STRING,
                                 SRC_PORT_STRING,
                                 SIZE_STRING,
                                 TTL_STRING,
                                 PROTOCOL_STRING,
                                 SEQ_NUM_STRING])

    return data

#read_packets("/Users/Leon/Documents/EA/NTLM-wenchao.pcap")