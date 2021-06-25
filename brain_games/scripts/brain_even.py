#!/usr/bin/env python3
"""It's a mini-game where user have to answer whether number is even or not."""

import random

import prompt

from brain_games.cli import welcome_user


def main():
    """Execute a mini-game."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt = 1
    while attempt <= 3:
        task = random.randint(0, 100)
        right_answer = 'yes' if task % 2 == 0 else 'no'
        print('Question: {0}'.format(str(task)))
        users_answer = prompt.string('Your answer: ')
        if right_answer != users_answer:
            print(
                "'{0}' is wrong answer ;(."
                "Correct answer was '{1}'.\n"
                "Let's try again, {2}!".format(users_answer, right_answer, name)
            )
            break
        elif right_answer == users_answer:
            print('Correct!')
        if attempt == 3:
            print('Congratulations, {0}!'.format(name))
        attempt += 1


if __name__ == '__main__':
    main()
