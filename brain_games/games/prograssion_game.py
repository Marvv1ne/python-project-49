from random import randint
from typing import Tuple


def find_lost_element() -> Tuple[str, str]:
    """This function create progression,
        hide  random element
        and return tuple of progression
        with hide elemend and this element"""
    first_element = randint(0, 100)
    step = randint(1, 10)
    progression_length = 10
    progression = [str(first_element + n) for n
                   in range(0, progression_length * step, step)]
    index = randint(0, 9)
    answer = progression[index]
    progression[index] = '..'
    return ' '.join(progression), answer
