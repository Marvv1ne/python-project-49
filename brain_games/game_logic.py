import prompt
from .cli import welcome_user
from typing import Callable

NUMBER_OF_QUESTIONS = 3


def game_start(function: Callable, question: str) -> None:
    """This function takes other function and question.
        Gives a hint on how to answer the question.
        Three questions are asked in the loop,
        if the answers to all questions are correct,
        then it print congratulations,
        else print correct answer and invites to play again"""
    name = welcome_user()
    print(question)
    for _ in range(NUMBER_OF_QUESTIONS):
        expression, correct_answer = function()
        print(f"Question: {expression}")
        answer = prompt.string("Your answer: ")
        if str(correct_answer) == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
