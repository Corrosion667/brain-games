"""It's a library of functions and variables for brain-even script."""

import random

MAX_RANDOM_NUMBER = 100

GAME_GOAL = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Define whether the number even or not.

    Args:
        number: Number for guessing by user.

    Returns:
        Answer whether number prime or not.
    """
    return (number % 2 == 0)


def iterate():
    """Game logic for cycle: question and right answer for the game.

    Returns:
        Right answer for game and question.
    """
    number = random.randint(0, MAX_RANDOM_NUMBER)
    question = str(number)
    if is_even(number):
        return ('yes', question)
    return ('no', question)
