"""It's a library of functions and variables for brain-prime script."""

import random

from brain_games.brain_engine import common_game

MAX_RANDOM_NUMBER = 50

GAME_GOAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(number):
    """Define whether the number prime or not.

    Args:
        number: Number for guessing by user.

    Returns:
        Answer whether number prime or not.
    """
    if number < 2:
        return 'no'
    if number == 2:
        return 'yes'
    for divider in range(2, number):
        if number % divider == 0:
            return 'no'
    return 'yes'


def game_iteration():
    """Game logic: question and right answer for the game.

    Returns:
        Right answer for game.
    """
    number = random.randint(2, MAX_RANDOM_NUMBER)
    print('Question: {0}'.format(str(number)))
    return check_prime(number)


def play_prime():
    """Program for the brain-prime script."""
    common_game(GAME_GOAL, game_iteration)
