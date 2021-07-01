"""It's a library of functions and variables for brain-prime script."""

import random

from brain_games.brain_engine import common_game

REASONABLE_LIMIT_OF_MENTAL_COMPUTATION = 50

game_goal = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(task):
    """Define wheter the number prime or not.

    Args:
        task: Number for guessing by user.

    Returns:
        Answer whether number prime or not.
    """
    if task <= 2:
        return 'no'
    for each in range(2, task):
        if task % each == 0:
            return 'no'
    return 'yes'


def game_iteration():
    """Game logic: question and right answer for the game.

    Returns:
        Right answer for game.
    """
    task = random.randint(2, REASONABLE_LIMIT_OF_MENTAL_COMPUTATION)
    print('Question: {0}'.format(str(task)))
    return check_prime(task)


def play_prime():
    """Program for the brain-prime script."""
    common_game(game_goal, game_iteration)
