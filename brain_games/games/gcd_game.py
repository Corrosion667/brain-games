"""It's a library of functions and variables for brain-gcd script."""

import random

from brain_games.brain_engine import common_game

MAX_RANDOM_NUMBER = 50

GAME_GOAL = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    """Find the greatest common divider for two numbers.

    Args:
        num1: First number.
        num2: Second number.

    Returns:
        The greatest common divider for num1 and num2.
    """
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 == num2:
        return num1
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2  # noqa: WPS350
        else:
            num2 = num2 % num1  # noqa: WPS350
    return (num1 + num2)


def game_iteration():
    """Game logic: question and right answer for the game.

    Returns:
        Right answer for game.
    """
    num1 = random.randint(0, MAX_RANDOM_NUMBER)
    num2 = random.randint(0, MAX_RANDOM_NUMBER)
    print('Question: {0} {1}'.format(str(num1), str(num2)))
    return gcd(num1, num2)


def play_gcd():
    """Program for the brain-gcd script."""
    common_game(GAME_GOAL, game_iteration)
