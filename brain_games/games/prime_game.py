"""It's a library of functions and variables for brain-prime script."""

import random

import prompt
from brain_games.cli import check_answer

REASONABLE_LIMIT_OF_MENTAL_COMPUTATION = 50


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


def play_prime(name):
    """Cycle for the brain-prime script.

    Args:
        name: Name of an user.
    """
    for attempt in range(1, 4):
        task = random.randint(2, REASONABLE_LIMIT_OF_MENTAL_COMPUTATION)
        print('Question: {0}'.format(str(task)))
        right_answer = check_prime(task)
        users_answer = prompt.string('Your answer: ')
        scenario = check_answer(users_answer, right_answer, name, attempt)
        if scenario == 'loose':
            break
