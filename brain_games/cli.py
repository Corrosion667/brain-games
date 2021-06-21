"""Command line interface for brain-games."""

import prompt


def welcome_user():
    """Ask user's name and use it."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
