import prompt
from random import randint


def is_even(number: int) -> bool:
    "function determines whether a number is even or not"
    return number % 2 == 0


def main() -> str:
    number = randint(0, 100)
    print('Answer "yes" if  number is even, otherwise answer "no".')
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    if ((is_even(number) and answer == 'yes') or (not is_even(number) and answer == 'no')):
        print('Correct!')
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {'yes' if is_even(number) else 'no'}")


if __name__ == "__main__":
    main()
