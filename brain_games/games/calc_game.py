from random import randint, choice
from typing import Tuple


def calc() -> Tuple[str, int]:
    """This function create random expression and
        return this expression and answer"""
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operator = choice(['+', '-', '*'])
    expression = f"{first_number} {operator} {second_number}"
    match operator:
        case '+':
            answer = first_number + second_number
        case '-':
            answer = first_number - second_number
        case '*':
            answer = first_number * second_number
    return expression, answer
