from random import uniform, randint


class FireWallTest():
    """
    this class tests a given firewall with pre-given data and ranks it
    :ivar clean_data: the clean data to be used to test fire walls (packets with no malicious intentions)
    (a DataFrame instance)
    :ivar malicious_data: the malicious data to be used to test fire walls (packets with malicious intentions)
    (a DataFrame instance)
    """
    # the number of good packets to test each time
    NUM_GOOD_PACKETS = 1000
    # the number of bad pakcets to test each time
    NUM_BAD_PACKETS = 1000

    def __init__(self, clean_data, malicious_data):
        """
        :param clean_data: the clean data to be used to test fire walls (packets with no malicious intentions)
        (a DataFrame instance)
        :param malicious_data: the malicious data to be used to test fire walls (packets with malicious intentions)
        (a DataFrame instance)
        """
        self.clean_data = clean_data
        self.malicious_data = malicious_data

    def get_fitness(self, fire_wall):
        """
        tests the fire wall we've built.
        we test what is the result for each packet (malicious and not), and then we score the fire wall
        according the result in the next way given:
        we mark the number of detected malicious packets as dm
        we mark the number of clean packets that were detected as malicious as mc
        1/((len(self.malicious_data)/dm) + (mc/len(self.clean_data)))
        :param fire_wall: the firewall to score
        :return: score between [0,1]
        """
        dm = 0  # num of detected malware packets
        mc = 0  # number of clean packets detected as malicous packets
        bad_index = 0 # randint(0,len(self.malicious_data) - FireWallTest.NUM_BAD_PACKETS)
        good_index = 0 # randint(0,len(self.clean_data) - FireWallTest.NUM_GOOD_PACKETS)

        good_packets_to_check = self.clean_data[good_index : good_index + FireWallTest.NUM_GOOD_PACKETS]
        bad_packets_to_check = self.malicious_data[bad_index : bad_index + FireWallTest.NUM_BAD_PACKETS]
        for _, mp in bad_packets_to_check.iterrows():
            dm += fire_wall.is_malicious(mp)
        for _, cp in good_packets_to_check.iterrows():
            mc += fire_wall.is_malicious(cp)

        print (dm, len(bad_packets_to_check), mc, len(good_packets_to_check))
        try:
            return 1.0 / ((len(bad_packets_to_check) / float(dm)) + (mc / float(len(good_packets_to_check))))
        except ZeroDivisionError:
            return 0
