from random import randint, choice
from typing import Tuple


def calc() -> Tuple[str, int]:
    """This function create random expression and
        return this expression and answer"""
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operator = choice(['+', '-', '*'])
    expression = f"{first_number} {operator} {second_number}"
    answer = eval(f"{first_number} {operator} {second_number}")
    return expression, answer
