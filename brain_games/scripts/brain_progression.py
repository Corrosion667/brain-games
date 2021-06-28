#!/usr/bin/env python3
"""It's a mini-game where user have to guess arithmetic progression element."""

import random

import prompt
from brain_games.cli import welcome_user


def main():
    """Execute a mini-game."""
    name = welcome_user()
    print('What number is missing in the progression?')
    max_length = 10
    max_step = 10
    max_start = 20
    attempt = 1
    while attempt <= 3:
        prog_length = random.randint(5, max_length)
        prog_step = random.randint(1, max_step)
        prog_start = random.randint(0, max_start)
        prog_substitute = random.randint(0, prog_length - 1)
        progression = ''
        for element in range(prog_length):
            if progression != '':
                progression += ' '
            if element == prog_substitute:
                progression += '..'
                continue
            progression += str(prog_start + element * prog_step)
        print('Question: {0}'.format(progression))
        users_answer = prompt.string('Your answer: ')
        right_answer = (prog_start + prog_substitute * prog_step)
        if str(right_answer) != users_answer:
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
