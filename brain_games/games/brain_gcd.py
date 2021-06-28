#!/usr/bin/env python3
"""It's a mini-game where user have to answer whether number is even or not."""

import math
import random

import prompt
from brain_games.cli import welcome_user


def main():
    """Execute a mini-game."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    attempt = 1
    while attempt <= 3:
        reasonable_limit_of_mental_computation = 50
        num1 = random.randint(0, reasonable_limit_of_mental_computation)
        num2 = random.randint(0, reasonable_limit_of_mental_computation)
        print('Question: {0} {1}'.format(str(num1), str(num2)))
        users_answer = prompt.string('Your answer: ')
        right_answer = math.gcd(num1, num2)
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
