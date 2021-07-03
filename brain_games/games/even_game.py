"""It's a library of functions and variables for brain-even script."""

import random

from brain_games.brain_engine import common_game

MAX_RANDOM_NUMBER = 100

GAME_GOAL = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_iteration():
    """Game logic: question and right answer for the game.

    Returns:
        Right answer for game.
    """
    task = random.randint(0, MAX_RANDOM_NUMBER)
    print('Question: {0}'.format(str(task)))
    return 'yes' if task % 2 == 0 else 'no'


def play_even():
    """Program for the brain-even script."""
    common_game(GAME_GOAL, game_iteration)
