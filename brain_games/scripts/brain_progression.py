from ..game_logic import game_start
from ..games.prograssion_game import find_lost_element


def main() -> str:
    question = "What number is missing in the progression?"
    game_start(find_lost_element, question)


if __name__ == "__main__":
    main()
