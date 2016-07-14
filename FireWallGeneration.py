from ParamVector import ParamVector
from Firewall import FireWall
from random import choice
from MemoizationUtils import *
from pathos.multiprocessing import ProcessingPool as Pool


class FireWallGeneration:
    """
    a class for representing a generation of firewalls
    :ivar firewalls: the firewalls that are in this generation, this ivar is a set
    """

    PROCESSES_NUM = 4  # the number of processes to use in order to calculate fitnesses
    process_pool = Pool(processes=PROCESSES_NUM)

    def __init__(self, param):
        """
        :param param: either the number of firewalls to create for the first generation or
        the firewalls to set to self, a set of firewalls
        init the first generation
        """
        if type(param) == int:
            self.num_of_firewalls = param
            self.firewalls = {FireWall(ParamVector.generate_random_data()) for _ in range(param)}
        elif type(param) == set:
            self.firewalls = param
            self.num_of_firewalls = len(param)

    def __repr__(self):
        """
        :return: a string representation of a firewall generation
        """
        gen_repr = ""
        for f in self.firewalls:
            gen_repr += str(f) + "\n"
        return gen_repr

    @staticmethod
    def _calculate_fitness_for_multi_firewalls(parmas):
        """
        :param params: a zipped containing the needed data
        :param params[0] = fitness_calculator: the instance of FireWallFitness to be used in order to calculate the fitness
        of the firewalls
        :param params[1] = firewalls: the firewalls to calculate the fitnesses for
        :return: a list, where the elemnt i is (firewalls[i], fitness of firewall[i])
        """
        fitness_calculator = parmas[0][0]
        firewalls = parmas[1][0]
        return [(fw, fitness_calculator.get_fitness(fw)) for fw in firewalls]

    def generate_next_generation(self, fitness_calculator, passing_num=12):
        """
        :param fitness_calculator: the instance of FireWallFitness to be used in order to calculate the fitness
        of the firewalls in the generation self
        :param passing_num: the number of firewalls to select in order to mate them into new firewalls
        :return: the next generation created using the firewalls in self
        """
        pool = FireWallGeneration.process_pool
        part_size = len(self.firewalls) / FireWallGeneration.PROCESSES_NUM
        ordered_firwalls = list(self.firewalls)
        firewall_parts = []
        for i in range(FireWallGeneration.PROCESSES_NUM):
            firewall_parts.append(ordered_firwalls[i * part_size: (i + 1) * part_size])

        results = pool.map(FireWallGeneration._calculate_fitness_for_multi_firewalls,
                           (zip([fitness_calculator, firewall_parts[0]]),
                            zip([fitness_calculator, firewall_parts[1]]),
                            zip([fitness_calculator, firewall_parts[2]]),
                            zip([fitness_calculator, firewall_parts[3]])))

        fitnesses = []
        [fitnesses.extend(r) for r in results]
        fitnesses.sort(key=lambda (fw, fitness): fitnesses)
        print "fitness: " + str(fitnesses[-1][1])
        print fitnesses[-1][0]

        selected_firewalls = [fw for (fw, _) in fitnesses[-passing_num:]]
        generated_firewall = []
        for _ in range(self.num_of_firewalls):
            fw_1 = choice(selected_firewalls)
            fw_2 = choice(selected_firewalls)
            new_firewall_params = FireWall.mate_param_vectors(fw_1.param_vector, fw_2.param_vector)
            new_firewall = FireWall(new_firewall_params)
            generated_firewall.append(new_firewall)
        return FireWallGeneration(set(generated_firewall))

    def write_self_to_file(self, path_file):
        """
        writes the string representation of self to the given file path
        :param path_file: the file path to save the data to
        :return: None
        """
        f = open(path_file, 'w')
        for fw in self.firewalls:
            f.write(str(fw) + "\n")
        f.close()

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
        f.close()
        return FireWallGeneration(fws)
