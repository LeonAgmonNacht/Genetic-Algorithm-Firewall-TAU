from FireWallGeneration import FireWallGeneration
from FireWallFitness import FireWallTest
from PacketDataParser import *

GENERATIONS_NUMBER = 10000
NUM_OF_FIREWALLS = 250
CLEAN_PACKETS_PCAP_FILE_PATH = "/Users/Leon/Documents/EA/NTLM-wenchao.pcap"
MALICIOUS_PACKETS_PCAP_FILE_PATH = "/Users/Leon/Documents/EA/NTLM-wenchao.pcap"


def read_malicious_packets():
    """
    reads the malicious packets from the path in constants
    :return: a DataFrame with the relevant data retrieved from the packets
    """
    return read_packets(MALICIOUS_PACKETS_PCAP_FILE_PATH)


def read_clean_packets():
    """
    reads the clean packets from the path in constants
    :return: a DataFrame with the relevant data retrieved from the packets
    """
    return read_packets(CLEAN_PACKETS_PCAP_FILE_PATH)


if __name__ == "__main__":
    fitness_factory = FireWallTest(read_clean_packets(),
                                   read_malicious_packets())
    generation = FireWallGeneration(param=NUM_OF_FIREWALLS)
    generation_counter = 0
    for _ in range(GENERATIONS_NUMBER):
        if generation_counter % 1000 == 0:
            generation.write_self_to_file("generations/Gen-"+str(generation_counter)+".txt")
            print generation_counter
        generation_counter += 1
        generation = generation.generate_next_generation(fitness_factory)