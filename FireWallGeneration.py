from ParamVector import ParamVector
from Firewall import FireWall
from random import choice
from MemoizationUtils import *

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
        self.num_of_firewalls = num_of_start_firewalls
        self.firewalls = {FireWall(ParamVector.generate_random_data()) for _ in range(num_of_start_firewalls)}

    def __init__(self, firewalls):
        """
        init self with firewalls
        :param firewalls: the firewalls to set to self, a set of firewalls
        """
        self.firewalls = firewalls
        self.num_of_firewalls = len(firewalls)

    def __repr__(self):
        """
        :return: a string representation of a firewall generation
        """
        gen_repr = ""
        for f in self.firewalls:
            gen_repr += str(f) + "\n"
        return gen_repr

    def generate_next_generation(self, fitness_calculator, passing_num = 15):
        """
        :param fitness_calculator: the instance of FireWallFitness to be used in order to calculate the fitness
        of the firewalls in the generation self
        :param passing_num: the number of firewalls to select in order to mate them into new firewalls
        :return: the next generation created using the firewalls in self
        """
        fitnesses = [(fw, fitness_calculator.get_fitness(fw)) for fw in self.firewalls]
        fitnesses.sort(key=lambda (fw, fitness): fitnesses)
        selected_firewalls = [fw for (fw, _) in fitnesses[-passing_num:]]
        generated_firewall = []
        for _ in range(self.num_of_firewalls):
            fw_1 = choice(selected_firewalls)
            fw_2 = choice(selected_firewalls)
            new_firewall = FireWall.mate_param_vectors(fw_1, fw_2)
            generated_firewall.append(new_firewall)

        mutated_firewalls = {FireWall(fw.param_vector.mutate()) for fw in generated_firewall}
        return FireWallGeneration(mutated_firewalls)

    def write_self_to_file(self, path_file):
        """
        writes the string representation of self to the given file path
        :param path_file: the file path to save the data to
        :return: None
        """
        f = open(path_file, 'w')
        for fw in self.firewalls:
            f.write(str(fw) + "\n")


    @staticmethod
    def load_from_file(file_path):
        """
        loads self using the data in the given file
        :param file_path: the path to the file that contains the data
        :return: a FireWallGeneration containing the data(firewalls) in the file
        """
        f = open(file_path, 'r')
        lines = f.readlines()
        fws = [get_firewall_from_string(line) for line in lines]
        return FireWallGeneration(fws)
