#!/usr/bin/env python3
"""It's a mini-game where user have to answer whether number is prime or not."""

import random

import prompt
from brain_games.cli import welcome_user


def main():
    """Execute a mini-game."""
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    attempt = 1
    reasonable_limit_of_mental_computation = 50
    while attempt <= 3:
        task = random.randint(2, reasonable_limit_of_mental_computation)
        print('Question: {0}'.format(str(task)))
        check = []
        for each in range(1, task + 1):
            if task % each == 0:
                check.append(each)
        right_answer = 'yes' if len(check) == 2 else 'no'
        users_answer = prompt.string('Your answer: ')
        if right_answer != users_answer:
            print(
                "'{0}' is wrong answer ;(."
                "Correct answer was '{1}'.\n"
                "Let's try again, {2}!".format(
                    users_answer, right_answer, name,
                ),
            )
            break
        elif right_answer == users_answer:
            print('Correct!')
        if attempt == 3:
            print('Congratulations, {0}!'.format(name))
        attempt += 1


if __name__ == '__main__':
    main()
