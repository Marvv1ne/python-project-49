#!/usr/bin/env python3
import prompt
from ..cli import welcome_user

NAME = prompt.string('May I have your name? ')


def main():
    welcome_user(NAME)


if __name__ == "__main__":
    main()
