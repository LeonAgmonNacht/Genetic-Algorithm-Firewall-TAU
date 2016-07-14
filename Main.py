from FireWallGeneration import FireWallGeneration
from FireWallFitness import FireWallTest
from PacketDataParser import *
from time import time
import cProfile

GENERATIONS_NUMBER = 100000
NUM_OF_FIREWALLS = 84
SAVE_TO_FILE_TIMES = 10
NUM_GOOD_PACKETS = 1000
NUM_BAD_PACKETS = 1000
CLEAN_PACKETS_CSV_FILE_PATH = "clean.csv"
MALICIOUS_PACKETS_CSV_FILE_PATH = "malicious.csv"
CLEAN_PACKETS_PCAP_FILE_PATH = "good.pcap"
MALICIOUS_PACKETS_PCAP_FILE_PATH = "bad.pcap"


def read_malicious_packets():
    """
    reads the malicious packets from the path in constants
    :return: a DataFrame with the relevant data retrieved from the packets
    """
    print "Loading Malware Packets..."
    # return read_packets(MALICIOUS_PACKETS_PCAP_FILE_PATH)
    return get_packets_from_csv(MALICIOUS_PACKETS_CSV_FILE_PATH)


def read_clean_packets():
    """
    reads the clean packets from the path in constants
    :return: a DataFrame with the relevant data retrieved from the packets
    """
    print "Loading Clean Packets..."
    # return read_packets(CLEAN_PACKETS_PCAP_FILE_PATH)
    return get_packets_from_csv(CLEAN_PACKETS_CSV_FILE_PATH)


def main():
    bad_packets = read_malicious_packets()
    # bad_packets.to_csv(MALICIOUS_PACKETS_CSV_FILE_PATH)
    clean_packets = read_clean_packets()
    # clean_packets.to_csv(CLEAN_PACKETS_CSV_FILE_PATH)

    fitness_factory = FireWallTest(clean_packets,
                                   bad_packets)

    print "Packets Loaded!"
    generation = FireWallGeneration(param=NUM_OF_FIREWALLS)
    generation_counter = 0
    for _ in range(GENERATIONS_NUMBER):
        if generation_counter % SAVE_TO_FILE_TIMES == 0:
            generation.write_self_to_file("generations/Gen-"+str(generation_counter)+".txt")
        generation_counter += 1
        start_time = time()
        generation = generation.generate_next_generation(fitness_factory)
        print str(generation_counter) + " with time: " + str(time() - start_time)

if __name__ == '__main__':
    # cProfile.run('main()')
    main()
