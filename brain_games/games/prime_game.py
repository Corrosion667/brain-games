"""It's a library of functions and variables for brain-prime script."""

import random

MAX_RANDOM_NUMBER = 50

GAME_GOAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Define whether the number prime or not.

    Args:
        number: Number for guessing by user.

    Returns:
        Answer whether number prime or not.
    """
    if number < 2:
        return False
    if number == 2:
        return True
    for divider in range(2, number):
        if number % divider == 0:
            return False
    return True


def iterate():
    """Game logic for cycle: question and right answer for the game.

    Returns:
        Right answer for game and question.
    """
    number = random.randint(2, MAX_RANDOM_NUMBER)
    question = str(number)
    if is_prime(number):
        return ('yes', question)
    return ('no', question)
