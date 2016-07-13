from ParamVector import ParamVector
from Firewall import FireWall


class FireWallGeneration:
    """
    a class for representing a generation of firewalls
    :ivar firewalls: the firewalls that are in this generation, this ivar is a set
    """
    def __init__(self, num_of_start_firewalls=100):
        """
        :param num_of_start_firewalls: the number of firewalls to create for the first generation
        init the first generation
        """
        self.firewalls = {FireWall(ParamVector.generate_random_data()) for _ in range(num_of_start_firewalls)}

    def generate_next_generation(fitness_calculator):
        """
        :param fitness_calculator: the instance of FireWallFitness to be used in order to calculate the fitness
        of the firewalls in the generation self
        :return: the next generation created using the firewalls in self
        """
        # TODO: read each new generation to file in order to be more robust #  Daniel:why? much slower...
        pass

    def write_self_to_file(self, path_file):
        """
        writes the string representation of self to the given file path
        :param path_file: the file path to save the data to
        :return: None
        """

    @staticmethod
    def load_from_file(file_path):
        """
        loads self using the data in the given file
        :param file_path: the path to the file that contains the data
        :return: a FireWallGeneration containing the data(firewalls) in the file
        """