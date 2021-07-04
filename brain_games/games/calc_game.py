"""It's a library of functions and variables for brain-calc script."""

import random

OPERATORS = ('+', '-', '*')
MAX_RANDOM_NUMBER = 20

GAME_GOAL = 'What is the result of the expression?.'


def find_answer(operator, num1, num2):
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


def iterate():
    """Game logic for cycle: question and right answer for the game.

    Returns:
        Right answer for game and question.
    """
    operator = random.choice(OPERATORS)
    num1 = random.randint(0, MAX_RANDOM_NUMBER)
    num2 = random.randint(0, MAX_RANDOM_NUMBER)
    question = '{0} {1} {2}'.format(str(num1), operator, str(num2))
    return (find_answer(operator, num1, num2), question)
