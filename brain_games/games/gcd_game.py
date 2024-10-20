from random import randint
from typing import Tuple


def find_gcd() -> Tuple[str, int]:
    """function finds the greatest common divisor of two numbers."""
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    expression = f"{number_1} {number_2}"
    while number_1 % number_2 != 0:
        number_1, number_2 = number_2, number_1 % number_2
        gcd = number_2
    return expression, gcd
