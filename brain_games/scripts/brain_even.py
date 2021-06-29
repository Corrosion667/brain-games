#!/usr/bin/env python3
"""It's a mini-game where user have to answer whether number is even or not."""

from brain_games.cli import welcome_user
from brain_games.games.even_game import play_even


def main():
    """Execute a mini-game."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play_even(name)


if __name__ == '__main__':
    main()
