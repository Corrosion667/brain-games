#!/usr/bin/env python3
"""It's a mini-game where user have to answer whether number is prime or not."""

from brain_games.cli import welcome_user
from brain_games.games.prime_game import play_prime


def main():
    """Execute a mini-game."""
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    play_prime(name)


if __name__ == '__main__':
    main()
