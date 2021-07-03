"""It's a library of functions and variables for brain-calc script."""

import random

from brain_games.brain_engine import common_game

OPERATORS = ('+', '-', '*')
REASONABLE_LIMIT_OF_MENTAL_COMPUTATION = 20

GAME_GOAL = 'What is the result of the expression?.'


def answer(operator, num1, num2):
    """Calculate the right answer depending on the randomised operand.

    Args:
        operator: Randomised one from operators list.
        num1: First randomised number in game.
        num2: Second randomised number in game.

    Returns:
        The right answer for the game.

    Raises:
        ValueError: if operand is unsupported.
    """
    if operator == '+':
        return (num1 + num2)
    elif operator == '-':
        return (num1 - num2)
    elif operator == '*':
        return (num1 * num2)
    raise ValueError('unsupported operand')


def game_iteration():
    """Game logic: question and right answer for the game.

    Returns:
        Right answer for game.
    """
    operator = random.choice(OPERATORS)
    num1 = random.randint(0, REASONABLE_LIMIT_OF_MENTAL_COMPUTATION)
    num2 = random.randint(0, REASONABLE_LIMIT_OF_MENTAL_COMPUTATION)
    print('Question: {0} {1} {2}'.format(str(num1), operator, str(num2)))
    return answer(operator, num1, num2)


def play_calc():
    """Program for the brain-calc script."""
    common_game(GAME_GOAL, game_iteration)
