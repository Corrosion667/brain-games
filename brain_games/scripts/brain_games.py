#!/usr/bin/env python3
"""Welcoming script."""

from brain_games.cli import welcome_user


def main():
    """Welcomes user with his name."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
