"""It's a library of functions and variables for brain-gcd script."""

import random

import prompt
from brain_games.cli import check_answer

REASONABLE_LIMIT_OF_MENTAL_COMPUTATION = 50


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


def play_gcd(name):  # noqa: WPS210
    """Cycle for the brain-gcd script.

    Args:
        name: Name of an user.
    """
    for attempt in range(1, 4):
        num1 = random.randint(0, REASONABLE_LIMIT_OF_MENTAL_COMPUTATION)
        num2 = random.randint(0, REASONABLE_LIMIT_OF_MENTAL_COMPUTATION)
        print('Question: {0} {1}'.format(str(num1), str(num2)))
        users_answer = prompt.string('Your answer: ')
        right_answer = gcd(num1, num2)
        scenario = check_answer(users_answer, right_answer, name, attempt)
        if scenario == 'loose':
            break
