"""Command line interface for brain-games common for every game."""

import prompt


def welcome_user():
    """Return name after asking it and greeting the user.

    Returns:
        Name of the user.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def loose(users_answer, right_answer, name):
    """Tell the player about loosing the game.

    Args:
        users_answer: An answer given by user.
        right_answer: An answer which is meant to be correct.
        name: Name of an user.
    """
    print(
        f"'{users_answer}' is wrong answer ;(. "
        + f"Correct answer was '{right_answer}'.\n"
        + f"Let's try again, {name}!",
    )


def check_answer(users_answer, right_answer, name, attempt):
    """Compare answers and execute winnig or loosing scenario.

    Args:
        users_answer: An answer given by user.
        right_answer: An answer which is meant to be correct.
        name: Name of an user.
        attempt: Number of current attempt durin the game.

    Returns:
        'Loose' to breake the gaming cycle.
    """
    if str(right_answer) == users_answer:
        print('Correct!')
        if attempt == 3:
            print('Congratulations, {0}!'.format(name))
    else:
        loose(users_answer, right_answer, name)
        return 'loose'
