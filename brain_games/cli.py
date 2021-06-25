"""Command line interface for brain-games."""

import prompt


def welcome_user():
    """Return name after asking it and greeting the user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
