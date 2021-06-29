#!/usr/bin/env python3
"""It's a mini-game where user have to find greatest common divisor ."""

from brain_games.cli import welcome_user
from brain_games.games.gcd_game import play_gcd


def main():
    """Execute a mini-game."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    play_gcd(name)


if __name__ == '__main__':
    main()
