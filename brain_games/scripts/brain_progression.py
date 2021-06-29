#!/usr/bin/env python3
"""It's a mini-game where user have to guess arithmetic progression element."""

from brain_games.cli import welcome_user
from brain_games.games.progression_game import play_progression


def main():
    """Execute a mini-game."""
    name = welcome_user()
    print('What number is missing in the progression?')
    play_progression(name)


if __name__ == '__main__':
    main()
