"""It's a library of functions and variables for brain-calc script."""

import random

import prompt
from brain_games.cli import check_answer

OPERANDS = ('+', '-', '*')
REASONABLE_LIMIT_OF_MENTAL_COMPUTATION = 20


def answer(operand, num1, num2):
    """Calculate the right answer depending on the randomised operand.

    Args:
        operand: Randomised one from operands list.
        num1: First randomised number in game.
        num2: second randomise number in game.

    Returns:
        The right answer for the game.

    Raises:
        ValueError: if operand is unsupported.
    """
    if operand == '+':
        return (num1 + num2)
    elif operand == '-':
        return (num1 - num2)
    elif operand == '*':
        return (num1 * num2)
    raise ValueError('unsupported operand')


def play_calc(name):  # noqa: WPS210
    """Cycle for the brain-calc script.

    Args:
        name: Name of an user.
    """
    for attempt in range(1, 4):
        operand = random.choice(OPERANDS)
        num1 = random.randint(0, REASONABLE_LIMIT_OF_MENTAL_COMPUTATION)
        num2 = random.randint(0, REASONABLE_LIMIT_OF_MENTAL_COMPUTATION)
        print('Question: {0} {1} {2}'.format(str(num1), operand, str(num2)))
        right_answer = answer(operand, num1, num2)
        users_answer = prompt.string('Your answer: ')
        scenario = check_answer(users_answer, right_answer, name, attempt)
        if scenario == 'loose':
            break
