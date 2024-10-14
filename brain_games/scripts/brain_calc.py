import prompt
from random import randint, choice
from ..cli import welcome_user
from .brain_games import NAME

NUMBER_OF_QUESTIONS = 3

def main():
    
    #operators = ['+', '-', '*']
    #first_number = randint(0, 100)
    #second_number = randint(0, 100)
    #print(first_number, choice(operators), second_number, eval(f"{first_number} {choice(operators)} {second_number}"))
    
    welcome_user(NAME)
    print("What is the result of the expression?")
    for _ in range(NUMBER_OF_QUESTIONS):
        first_number = randint(0, 100)
        second_number = randint(0, 100)
        operator = choice(['+', '-', '*'])
        print(f"Question: {first_number} {operator} {second_number}")
        answer = prompt.string("Your answer: ")
        correct_answer = eval(f"{first_number} {operator} {second_number}")
        if int(answer) == correct_answer:
            print("Correct")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.",
                  f"Let's try again, {NAME}!")
            break
    else:
        print(f"Congratulations, {NAME}")
        


if __name__ == "__main__":
    main()
