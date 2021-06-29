#!/usr/bin/env python3
"""It's a mini-game where user have to execute some simple math operations."""

from brain_games.cli import welcome_user
from brain_games.games.calc_game import play_calc


def main():
    """Execute a mini-game."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?.')
    play_calc(name)


if __name__ == '__main__':
    main()
