from random import randint

def is_even() -> str:
    """function return 'yes' if number is even or return 'no'"""
    number = randint(0, 100)
    return number, "yes" if number % 2 == 0 else 'no'