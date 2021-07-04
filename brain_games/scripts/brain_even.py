#!/usr/bin/env python3
"""It's a mini-game where user have to answer whether number is even or not."""

from brain_games.brain_engine import play_game
from brain_games.games.even_game import GAME_GOAL, iterate


def main():
    """Execute a mini-game."""
    play_game(GAME_GOAL, iterate)


if __name__ == '__main__':
    main()
