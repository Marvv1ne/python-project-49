from random import randint, choice
from ...game_logic import game_start


def calc() -> str:
    """here must be docstring of function"""
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operator = choice(['+', '-', '*'])
    expression = f"{first_number} {operator} {second_number}"
    answer = eval(f"{first_number} {operator} {second_number}")
    return expression, answer

def main():
    question = "What is the result of the expression?"
    game_start(calc, question)
        


if __name__ == "__main__":
    main()
