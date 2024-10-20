from ..game_logic import game_start
from ..games.is_prime_game import is_prime_game


def main():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_start(is_prime_game, question)


if __name__ == "__main__":
    main()
