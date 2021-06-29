"""It's a library of functions and variables for brain-prime script."""

import random

import prompt
from brain_games.cli import check_answer

reasonable_limit_of_mental_computation = 50


def check(task):
    """Create a list for prime-check of the randomised number.

    Args:
        task: Randomised number for guessing by user.

    Returns:
        List of numbers by which randomised is divisible without a remainder.
    """
    check_list = []
    for each in range(1, task + 1):
        if task % each == 0:
            check_list.append(each)
    return len(check_list)


def play_prime(name):
    """Cycle for the brain-prime script.

    Args:
        name: Name of an user.
    """
    for attempt in range(1, 4):
        task = random.randint(2, reasonable_limit_of_mental_computation)
        print('Question: {0}'.format(str(task)))
        right_answer = 'yes' if check(task) == 2 else 'no'
        users_answer = prompt.string('Your answer: ')
        scenario = check_answer(users_answer, right_answer, name, attempt)
        if scenario == 'loose':
            break
