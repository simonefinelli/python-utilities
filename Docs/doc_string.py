"""Example of DocString usage."""
import random


# Function
def weird_sum(n1: int, n2: int) -> float:
    """Sum two integer.

    The function sums two integers and subtracts a random float number
    between 0 and 1.

    :param n1: First integer number
    :type n1: int
    :param n2: Second integer number
    :type n2: int

    :return: the sum of two integer
    :rtype: int

    """
    sum = n1 + n2
    random_n = random.random()
    print(random_n)
    sum -= random_n

    return sum
