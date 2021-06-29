"""It's a library of functions and variables for brain-even script."""

import random

import prompt
from brain_games.cli import check_answer

reasonable_limit_of_mental_computation = 100


def play_even(name):
    """Cycle for the brain-even script.

    Args:
        name: Name of an user.
    """
    for attempt in range(1, 4):
        task = random.randint(0, reasonable_limit_of_mental_computation)
        right_answer = 'yes' if task % 2 == 0 else 'no'
        print('Question: {0}'.format(str(task)))
        users_answer = prompt.string('Your answer: ')
        scenario = check_answer(users_answer, right_answer, name, attempt)
        if scenario == 'loose':
            break
