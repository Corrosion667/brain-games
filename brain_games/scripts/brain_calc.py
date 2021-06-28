#!/usr/bin/env python3
"""It's a mini-game where user have to execute some simple math operations."""

import random

import prompt
from brain_games.cli import welcome_user


def main():
    """Execute a mini-game."""
    name = welcome_user()
    print('What is the result of the expression?.')
    operands = ['+', '-', '*']
    attempt = 1
    while attempt <= 3:
        action = random.choice(operands)
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        print('Question: {0} {1} {2}'.format(str(num1), action, str(num2)))
        if action == '+':
            right_answer = num1 + num2
        elif action == '-':
            right_answer = num1 - num2
        else:
            right_answer = num1 * num2
        users_answer = prompt.string('Your answer: ')
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
