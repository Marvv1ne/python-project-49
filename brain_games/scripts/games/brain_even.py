from random import randint
from ...game_logic import game_start


def is_even() -> str:
    """function return 'yes' if number is even or return 'no'"""
    number = randint(0, 100)
    return number, "yes" if number % 2 == 0 else 'no'


def main() -> str:
    question = "Answer 'yes' if  number is even, otherwise answer 'no'."
    game_start(is_even, question)


if __name__ == "__main__":
    main()
