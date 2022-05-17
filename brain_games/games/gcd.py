#!/usr/bin/env python3.10
import random
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def solution():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = gcd(number1, number2)
    return correct_answer, question
