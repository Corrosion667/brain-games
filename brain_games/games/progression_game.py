"""It's a library of functions and variables for brain-progression script."""

import random

import prompt
from brain_games.cli import check_answer

MAX_LENGTH = 10
MAX_STEP = 10
MAX_START = 20


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


def play_progression(name):  # noqa: WPS210
    """Cycle for the brain-prime script.

    Args:
        name: Name of an user.
    """
    for attempt in range(1, 4):
        prog_length = random.randint(5, MAX_LENGTH)
        prog_step = random.randint(1, MAX_STEP)
        prog_start = random.randint(0, MAX_START)
        prog_substitute = random.randint(0, prog_length - 1)
        progression = make_prog(
            prog_start, prog_length, prog_step, prog_substitute,
        )
        print('Question: {0}'.format(progression))
        users_answer = prompt.string('Your answer: ')
        right_answer = (prog_start + prog_substitute * prog_step)
        scenario = check_answer(users_answer, right_answer, name, attempt)
        if scenario == 'loose':
            break
