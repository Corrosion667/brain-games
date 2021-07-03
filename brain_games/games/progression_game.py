"""It's a library of functions and variables for brain-progression script."""

import random

from brain_games.brain_engine import common_game

MAX_LENGTH = 10
MAX_STEP = 10
MAX_START = 20

GAME_GOAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_prog(prog_start, prog_length, prog_step, prog_substitute):
    """Create and return a progression to be guessed.

    Args:
        prog_start: Starting element of progression.
        prog_length: Length of progression.
        prog_step: How much the next element is larger than the previous.
        prog_substitute: Number of element to be hidden.

    Returns:
        Made progression.
    """
    progression = []
    for element in range(prog_length):
        if element == prog_substitute:
            progression.append('..')
            continue
        progression.append(str(prog_start + element * prog_step))
    return ' '.join(progression)


def game_iteration():
    """Game logic: question and right answer for the game.

    Returns:
        Right answer for game.
    """
    prog_length = random.randint(5, MAX_LENGTH)
    prog_step = random.randint(1, MAX_STEP)
    prog_start = random.randint(0, MAX_START)
    prog_substitute = random.randint(0, prog_length - 1)
    progression = make_prog(
        prog_start, prog_length, prog_step, prog_substitute,
    )
    print('Question: {0}'.format(progression))
    return (prog_start + prog_substitute * prog_step)


def play_progression():
    """Program for the brain-progression script."""
    common_game(GAME_GOAL, game_iteration)
