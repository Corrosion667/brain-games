#!/usr/bin/env python3
"""It's a mini-game where user have to guess arithmetic progression element."""

from brain_games.brain_engine import play_game
from brain_games.games.progression_game import GAME_GOAL, get_task


def main():
    """Execute a mini-game."""
    play_game(GAME_GOAL, get_task)


if __name__ == '__main__':
    main()
