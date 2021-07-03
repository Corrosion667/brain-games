"""It's a library of functions and variables for brain-progression script."""

import random

from brain_games.brain_engine import play_game

MAX_LENGTH = 10
MAX_STEP = 10
MAX_START = 20

GAME_GOAL = 'What number is missing in the progression?'


def make_prog(start, length, step, index_missing):
    """Create and return a progression to be guessed.

    Args:
        start: Starting element of progression.
        length: Length of progression.
        step: How much the next element is larger than the previous.
        index_missing: Element of progression to be hidden and guessed.

    Returns:
        Made progression.
    """
    progression = []
    for index in range(length):
        if index == index_missing:
            progression.append('..')
            continue
        progression.append(str(start + index * step))
    return ' '.join(progression)


def iterate():
    """Game logic for cycle: question and right answer for the game.

    Returns:
        Right answer for game.
    """
    length = random.randint(5, MAX_LENGTH)
    step = random.randint(1, MAX_STEP)
    start = random.randint(0, MAX_START)
    index_missing = random.randint(0, length - 1)
    progression = make_prog(
        start, length, step, index_missing,
    )
    print('Question: {0}'.format(progression))
    return (start + index_missing * step)


def play_progression():
    """Program for the brain-progression script."""
    play_game(GAME_GOAL, iterate)
