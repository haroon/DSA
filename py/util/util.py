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

def make_comparator(ascending):
    """Create a comparison function that compares two variables in ascending or descending order.

    Attributes:
        ascending (bool): Whether comparison is ascending or descending.

    Returns:
        Comparison function that compares two items.
    """
    return lambda x, y: x > y if ascending else y > x