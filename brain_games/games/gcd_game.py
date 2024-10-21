from random import randint
from typing import Tuple


def is_divisible(devidend: int, devider: int):
    """This function return True if numbers
       are divisible without remainder"""
    return devidend % devider == 0


def find_gcd() -> Tuple[str, int]:
    """function finds the greatest common divisor of two numbers."""
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    expression = f"{number_1} {number_2}"
    while not is_divisible(number_1, number_2):
        number_1, number_2 = number_2, number_1 % number_2
        gcd = number_2
    return expression, gcd
