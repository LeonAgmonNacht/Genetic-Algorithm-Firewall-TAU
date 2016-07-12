# Created by Leon Agmon Nacht

from scapy.all import rdpcap


class DataVector(object):
    """
    1a class representing a relevant data from a single packet. the data is:
    Source IP address
    Destination IP address
    Source port number
    Destination port number
    Size of packet
    Time to Live (TTL)
    Packet type
    Sequence number
    Number of hops between the source and destination (not available currently)
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


class PCAPData(object):
    """
    a class representing the data in a PCAP file
    use example: packets = PCAPData("/Users/Leon/Documents/EA/NTLM-wenchao.pcap")
    """
    def __init__(self, path_to_pcap):
        """
        init with a path to a pcap file to load the data from
        :param path_to_pcap: path to file
        :return: a new created instance
        """
        self.packets = []  # the packets of the given pcap file as a DataVector
        pcap_data = rdpcap(path_to_pcap)
        for p in pcap_data:
            self.packets.append(DataVector(p))