"""It's a library of functions and variables for brain-even script."""

import random

from brain_games.brain_engine import play_game

MAX_RANDOM_NUMBER = 100

GAME_GOAL = 'Answer "yes" if the number is even, otherwise answer "no".'


def iterate():
    """Game logic for cycle: question and right answer for the game.

    Returns:
        Right answer for game.
    """
    number = random.randint(0, MAX_RANDOM_NUMBER)
    print('Question: {0}'.format(str(number)))
    return 'yes' if number % 2 == 0 else 'no'


def play_even():
    """Program for the brain-even script."""
    play_game(GAME_GOAL, iterate)
