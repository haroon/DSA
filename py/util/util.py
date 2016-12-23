from datetime import datetime
from random import random, seed

def get_random_int_list(size=10, mult=1000):
    """Generate a list of *random* integers.

    Attributes:
        size (int): Size of the list
        mult (int): Value multiplier for random numbers.
    Returns:
        List of pseudo random integers.
    """
    seed(datetime.now())
    return [int(random() * mult) for i in range(size)]