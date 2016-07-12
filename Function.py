from random import random


class Function:
    """
    A class representing a function.
    This class improves the work with functions like in math
    Note: This class is immutable, f + g returns a new function and is not changing any function.
    """
    def __init__(self, param):
        """
        This is the constructor for the function object.
        :param param: the function this object represents (with def or lambda) or an int for a constant function.
        """
        if type(param) == int:
            self.function = lambda x: param
        else:
            self.function = param

    def __call__(self, param):
        """
        This function is not to be used directly, but allows the user to call it like a function
        Example: f(2)
        :param param: the parameter to be used with the function
        :return: function(parameter)
        """
        return self.function(param)

    def __neg__(self):
        """
        This function is not to be used directly, but allows the user to get the negative of this function
        :return: the negative function (-f)
        """
        return Function(lambda x: -self(x))

    def __add__(self, other):
        """
        This function is not to be used directly, but allows the user to use the operator "+"
        :param other: a function or a constant to add to the function.
        :return: a new function which for every f and g: (f+g)(x) = f(x) + g(x)
        """
        if type(other) == int:
            return self + Function(other)
        return Function(lambda x: self(x) + other(x))

    def __sub__(self, other):
        """
        This function is not to be used directly, but allows the user to use the operator "-"
        :param other: a function or a constant to sub from the function.
        :return: a new function which for every f and g: (f-g)(x) = f(x) - g(x)
        """
        return self + (-other)

    def __mul__(self, other):
        """
        This function is not to be used directly, but allows the user to use the operator "*"
        :param other: a function or a constant to mul with the function
        :return: a new function which for every f and g: (f*g)(x) = f(x) * g(x)
        """
        if type(other) == int:
            return Function(lambda x: self(x) * other)
        return Function(lambda x: self(x) * other(x))

    def __div__(self, other):
        """
        This function is not to be used directly, but allows the user to use the operator "/"
        :param other: a function or a constant to div with the function
        :return: a new function which for every f and g: (f/g)(x) = f(x) / g(x)
        """
        if type(other) == int:
            return Function(lambda x: self(x) / other)
        return Function(lambda x: self(x) / other(x))

    def __truediv__(self, other):
        """
        This function is not to be used directly, but allows the user to use the operator "//"
        :param other: a function or a constant to truediv with the function
        :return: a new function which for every f and g: (f//g)(x) = f(x) // g(x)
        """
        if type(other) == int:
            return Function(lambda x: self(x) // other)
        return Function(lambda x: self(x) // other(x))

    def __pow__(self, other):
        """
        This function is not to be used directly, but allows the user to use the operator "**"
        :param other: a function or a constant to pow with the function
        :return: a new function which for every f and g: (f**g)(x) = f(x) ** g(x)
        """
        if type(other) == int:
            f = self
            for i in range(other - 1):
                f *= self
            return f
        else:
            return lambda x: self(x) ** other(x)

    def __xor__(self, other):
        """
        This function is not to be used directly, but allows the user to use the operator "^"
        :param other: a function to be composed with the function
        :return: a new function which for every f ang g: (f^g)(x) = f(g(x))
        """
        if type(other) == int:
            return self ^ Function(other)
        return Function(lambda x: self(other(x)))


class ProbabilityException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FunctionWithProbability(Function):
    """
    This class extends the function class and adds the probability to be chosen modifier to it
    """
    def __init__(self, param, probability):
        """
        :param param: The param which this object represents.
        :param probability: The probability of being chosen from a set of functions.
        """
        if type(param) == int:
            self.function = lambda x: param
        else:
            self.function = param
        if (probability < 0 or probability > 1):
            raise ProbabilityException("Probability must be between 0 and 1")
        self.probability = probability


def get_func_from_set(set):
    """
    This function picks a random function from a set of functions, but it picks it
    with different probability for each function, chosen by the function itself.
    :param set: The set of functions that the function is picked from.
    :return:
        If not all functions in the set are FunctionWithProbability the function will assert
        If the sum of probabilities is not 1 the function will raise ProbabilityException
        Else it just returns a random function from the set.
    """
    sum_probs = 0
    for func in set:
        assert isinstance(func, FunctionWithProbability)
        sum_probs += func.probability

    sum_probs = 0
    rand_num = random()
    for func in set:
        sum_probs += func.probability
        if rand_num <= sum_probs:
            return func
