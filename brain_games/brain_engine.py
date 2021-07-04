"""The common engine to run custom games."""

import prompt

ATTEMPTS = 3


def welcome_user():
    """Return name after asking it and greeting the user.

    Returns:
        Name of the user.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def check_answer(users_answer, right_answer, name, attempt):
    """Compare answers and execute winnig or loosing scenario.

    Args:
        users_answer: An answer given by user.
        right_answer: An answer which is meant to be correct.
        name: Name of the user.
        attempt: Number of current round in the game.

    Returns:
        'Loose' to breake the gaming cycle.
    """
    if str(right_answer) == users_answer:
        print('Correct!')
        if attempt == ATTEMPTS:
            print('Congratulations, {0}!'.format(name))
    else:
        print(
            f"'{users_answer}' is wrong answer ;(. "
            + f"Correct answer was '{right_answer}'.\n"
            + f"Let's try again, {name}!",
        )
        return 'loose'


def play_game(game_goal, iterate):
    """Run a custom brain game.

    Args:
        game_goal: playing condition of a certain game.
        iterate: Determine question and right answer during each round of game.
    """
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game_goal)
    for attempt in range(1, ATTEMPTS + 1):
        task = iterate()
        print('Question: {0}'.format(task[1]))
        users_answer = prompt.string('Your answer: ')
        scenario = check_answer(users_answer, task[0], name, attempt)
        if scenario == 'loose':
            break
