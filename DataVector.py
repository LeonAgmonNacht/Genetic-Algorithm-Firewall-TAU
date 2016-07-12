# Created by Leon Agmon Nacht

from scapy.all import rdpcap


class DataVector(object):
    """
    a class representing a relevant data from a single packet. the data is:
    Source IP address
    Destination IP address
    Source port number
    Destination port number
    Size of packet
    Time to Live (TTL)
    Packet type
    Sequence number
    """

    def __init__(self, sc_packet):
        """
        init with a scapy packet
        :param sc_packet: the packet to get the data from
        :return: a new instance holding the wanted data from the scapy packet
        """
        self.dstIP = sc_packet.dst
        self.srcIP = sc_packet.src
        self.dstPort = sc_packet.dport
        self.srcPort = sc_packet.sport
        self.size = len(sc_packet)
        self.ttl = sc_packet.ttl
        layer_index = 1

        # get upper layer in packet:

        while True:
            try:
                self.protocol = sc_packet[layer_index].name
                layer_index += 1
            except Exception:
                break
        self.protocol = sc_packet[layer_index - 1].name


def get_packets_from_pcap(pcap_path):
    """
    receives the packets from the given file path
    :param pcap_path: the path to the pcap file to load the data from
    :return: list of DataVectors holding the data in the pcap file
    """
    packets = []  # the packets of the given pcap file as a DataVector
    pcap_data = rdpcap(pcap_path)
    for p in pcap_data:
        packets.append(DataVector(p))
    return packets