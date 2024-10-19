from ..game_logic import game_start
from ..games.is_prime_game import is_prime


def main() -> str:
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_start(is_prime, question)


if __name__ == "__main__":
    main()
