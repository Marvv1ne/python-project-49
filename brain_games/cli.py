import prompt


def welcome_user() -> None:
    """The function takes a string with a name and prints a greeting"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name
