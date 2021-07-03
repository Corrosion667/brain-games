#!/usr/bin/env python3
"""It's a mini-game where user have to execute some simple math operations."""

from brain_games.brain_engine import common_game
from brain_games.games.calc_game import GAME_GOAL, iterate


def main():
    """Execute a mini-game."""
    common_game(GAME_GOAL, iterate)


if __name__ == '__main__':
    main()
