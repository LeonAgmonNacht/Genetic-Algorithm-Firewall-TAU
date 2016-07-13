from FireWallGeneration import FireWallGeneration
from FireWallFitness import FireWallTest
GENERATIONS_NUMBER = 10000
NUM_OF_FIREWALLS = 250

def read_malicious_packets():
    """
    reads the malicious packets from the path in constants
    :return: a list with the data of the malicious packets as DataVector
    """
    pass


def read_clean_packets():
    """
    reads the clean packets from the path in constants
    :return: a list with the data of the clean packets as DataVector
    """
    pass


if __name__ == "__main__":
    fitness_factory = FireWallTest({}, {})
    generation = FireWallGeneration(param=NUM_OF_FIREWALLS)
    generation_counter = 0
    for _ in range(GENERATIONS_NUMBER):
        if generation_counter % 1000 == 0:
            generation.write_self_to_file("generations/Gen-"+str(generation_counter)+".txt")
            print generation_counter
        generation_counter += 1
        generation = generation.generate_next_generation(fitness_factory)