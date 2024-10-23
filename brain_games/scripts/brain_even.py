from ..game_logic import game_start
from ..games.is_even_game import is_even


def main():
    question = "Answer 'yes' if number is even, otherwise answer 'no'."
    game_start(is_even, question)


if __name__ == "__main__":
    main()
