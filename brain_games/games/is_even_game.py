from random import randint
from typing import Tuple


def is_even() -> Tuple[int, str]:
    """function return 'yes' if number is even or return 'no'"""
    number = randint(1, 100)
    return number, "yes" if number % 2 == 0 else 'no'