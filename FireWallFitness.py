class FireWallTest():
    """
    this class tests a given firewall with pre-given data and ranks it
    :ivar clean_data: the clean data to be used to test fire walls (packets with no malicious intentions)
    :ivar malicious_data: the malicious data to be used to test fire walls (packets with malicious intentions)
    """
    def __init__(self, clean_data, malicious_data):
        """
        :param clean_data: the clean data to be used to test fire walls (packets with no malicious intentions)
        :param malicious_data: the malicious data to be used to test fire walls (packets with malicious intentions)
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
        pass

