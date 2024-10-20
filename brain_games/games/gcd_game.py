from random import randint
from typing import Tuple


def find_gcd() -> Tuple[str, int]:
    """function finds the greatest common divisor of two numbers."""
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    expression = f"{first_number} {second_number}"
    
    while first_number % second_number != 0:
        first_number, second_number = second_number, first_number % second_number
        gcd = second_number
    return expression, gcd