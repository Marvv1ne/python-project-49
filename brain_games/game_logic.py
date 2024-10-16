import prompt
from .scripts.brain_games import NAME
from .cli import welcome_user
from typing import Callable

NUMBER_OF_QUESTIONS = 3

def game_start(function: Callable, question : str):
    welcome_user(NAME)
    print(question)
    for _ in range(NUMBER_OF_QUESTIONS):
        expression, correct_answer = function()
        print(f"Question: {expression}")
        answer = prompt.string("Your answer: ")
        if str(correct_answer) == answer:
            print(f"Your answer: '{answer}'")
            print('Correct!')            
        else:
            print(f"'{answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {NAME}!")
            break
    else:
        print(f"Congratulations, {NAME}")


