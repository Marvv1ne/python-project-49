from ..game_logic import game_start
from .games.gcd_game import find_gcd

def main() -> str:
    question = "Find the greatest common divisor of given numbers."
    game_start(find_gcd, question)


if __name__ == "__main__":
    main()