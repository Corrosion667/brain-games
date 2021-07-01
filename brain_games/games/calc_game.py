"""It's a library of functions and variables for brain-calc script."""

import random

from brain_games.brain_engine import common_game

OPERANDS = ('+', '-', '*')
REASONABLE_LIMIT_OF_MENTAL_COMPUTATION = 20

game_goal = 'What is the result of the expression?.'


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


def game_iteration():
    """Game logic: question and right answer for the game.

    Returns:
        Right answer for game.
    """
    operand = random.choice(OPERANDS)
    num1 = random.randint(0, REASONABLE_LIMIT_OF_MENTAL_COMPUTATION)
    num2 = random.randint(0, REASONABLE_LIMIT_OF_MENTAL_COMPUTATION)
    print('Question: {0} {1} {2}'.format(str(num1), operand, str(num2)))
    return answer(operand, num1, num2)


def play_calc():
    """Program for the brain-calc script."""
    common_game(game_goal, game_iteration)
