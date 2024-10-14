import prompt
from random import randint
from ..cli import welcome_user
from .brain_games import NAME


def is_even(number: int) -> bool:
    "function determines whether a number is even or not"
    return number % 2 == 0


def main() -> str:
    counter_of_correct_answers = 0
    welcome_user(NAME)
    print('Answer "yes" if  number is even, otherwise answer "no".')
    while counter_of_correct_answers < 3:
        number = randint(0, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if ((is_even(number) and answer == 'yes') or
            (not is_even(number) and answer == 'no')):
            print(f"Your answer: '{'yes' if is_even(number) else 'no'}'")
            print('Correct!')
            counter_of_correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(.",
                  f"Correct answer was '{'yes' if is_even(number) else 'no'}'")
            print(f"Let's try again, {NAME}!")
            break
    if counter_of_correct_answers == 3:
        print(f"Congratulations, {NAME}")


if __name__ == "__main__":
    main()
