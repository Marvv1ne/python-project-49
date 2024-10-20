from ..game_logic import game_start
from ..games.calc_game import calc


def main():
    question = "What is the result of the expression?"
    game_start(calc, question)


if __name__ == "__main__":
    main()
