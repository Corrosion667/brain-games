"""It's a library of functions and variables for brain-gcd script."""

import random

MAX_RANDOM_NUMBER = 50

GAME_GOAL = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    """Find the greatest common divider for two numbers.

    Args:
        num1: First number.
        num2: Second number.

    Returns:
        The greatest common divider for num1 and num2.
    """
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2  # noqa: WPS350
        else:
            num2 = num2 % num1  # noqa: WPS350
    return (num1 + num2)


def iterate():
    """Game logic for cycle: question and right answer for the game.

    Returns:
        Right answer for game.
    """
    num1 = random.randint(0, MAX_RANDOM_NUMBER)
    num2 = random.randint(0, MAX_RANDOM_NUMBER)
    question = '{0} {1}'.format(str(num1), str(num2))
    return (find_gcd(num1, num2), question)
