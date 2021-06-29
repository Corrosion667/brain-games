"""It's a library of functions and variables for brain-gcd script."""

import math
import random

import prompt
from brain_games.cli import check_answer

reasonable_limit_of_mental_computation = 50


def play_gcd(name):  # noqa: WPS210
    """Cycle for the brain-gcd script.

    Args:
        name: Name of an user.
    """
    for attempt in range(1, 4):
        num1 = random.randint(0, reasonable_limit_of_mental_computation)
        num2 = random.randint(0, reasonable_limit_of_mental_computation)
        print('Question: {0} {1}'.format(str(num1), str(num2)))
        users_answer = prompt.string('Your answer: ')
        right_answer = math.gcd(num1, num2)
        scenario = check_answer(users_answer, right_answer, name, attempt)
        if scenario == 'loose':
            break
