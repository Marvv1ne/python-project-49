from random import randint
from typing import Tuple


def is_prime(number: int) -> bool:
    """This function checks whether
        a number is prime or not"""
    for n in range(2, number // 2):
        if number % n == 0:
            return False
    return True


def is_prime_game() -> Tuple[int, str]:
    """function return 'yes' if number is prime or return 'no'"""
    number = randint(0, 100)
    if number <= 1 or not is_prime(number):
        return number, "no"
    else:
        return number, "yes"
