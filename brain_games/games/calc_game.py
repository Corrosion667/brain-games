"""It's a library of functions and variables for brain-calc script."""

import random

import prompt
from brain_games.cli import check_answer

operands = ['+', '-', '*']
reasonable_limit_of_mental_computation = 20


def answer(operand, num1, num2):
    """Calculate the right answer depending on the randomised operand.

    Args:
        operand: Randomised one from operands list.
        num1: First randomised number in game.
        num2: second randomise numbe in game.

    Returns:
        The right answer for the game.
    """
    if operand == '+':
        right_answer = num1 + num2
    elif operand == '-':
        right_answer = num1 - num2
    else:
        right_answer = num1 * num2
    return right_answer


def play_calc(name):  # noqa: WPS210
    """Cycle for the brain-calc script.

    Args:
        name: Name of an user.
    """
    for attempt in range(1, 4):
        operand = random.choice(operands)
        num1 = random.randint(0, reasonable_limit_of_mental_computation)
        num2 = random.randint(0, reasonable_limit_of_mental_computation)
        print('Question: {0} {1} {2}'.format(str(num1), operand, str(num2)))
        right_answer = answer(operand, num1, num2)
        users_answer = prompt.string('Your answer: ')
        scenario = check_answer(users_answer, right_answer, name, attempt)
        if scenario == 'loose':
            break
