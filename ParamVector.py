class ParamVector(object):
    """
    This class represents the vectors that defines a firewall
    a ParamVector is a class that represents a vector that defines a firewall.
    we have our indicator functions that should get parameters, lets call these functions g1...gn
    for each gi we can say that there is a vector (ai1,...,aim) of scalars. so we can represent every firewall Fl
    as the sum of Fi^gi  where Fi is a mutate function.
    so we can think about a vector of different sized vectors, where every vector i is:
    fi, ai1,...aim
    """
    # the functions that can be used to mutate a ParamVector, instances of ProbabilityFunction
    mutate_functions = []

    @staticmethod
    def generate_random_data():
        """
        creates a ParamVector with random data
        :return: an instance of ParamVector that is defined using random data
        """
        pass