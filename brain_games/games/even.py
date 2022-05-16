#!/usr/bin/env python3.10
import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    """Check if given number is even."""
    return number % 2 == 0


def solution():
    number = random.randint(1, 100)
    if is_even(number):
        correct_answer = 'yes'
        return number, correct_answer
    else:
        correct_answer = 'no'
        return number, correct_answer




