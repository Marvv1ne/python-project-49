from random import randint

def is_prime() -> str:
    """function return 'yes' if number is even or return 'no'"""
    number = randint(0, 100)
    if number <= 1:
        return number, "no"
    
    for n in range(2, number // 2):
        if number % 2 == 0:
            return number, "no"
    return number, "yes"