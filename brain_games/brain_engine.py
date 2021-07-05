"""The common engine to run custom games."""

import prompt

ATTEMPTS_COUNT = 3


def play_game(game_goal, iterate):
    """Run a custom brain game.

    Args:
        game_goal: playing condition of a certain game.
        iterate: Determine right answer and question during each round of game.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game_goal)
    for _ in range(0, ATTEMPTS_COUNT):
        right_answer, question = iterate()
        print('Question: {0}'.format(question))
        users_answer = prompt.string('Your answer: ')
        if str(right_answer) == users_answer:
            print('Correct!')
        else:
            print(
                f"'{users_answer}' is wrong answer ;(. "
                + f"Correct answer was '{right_answer}'.\n"
                + f"Let's try again, {name}!",
            )
            break
    else:
        print('Congratulations, {0}!'.format(name))
