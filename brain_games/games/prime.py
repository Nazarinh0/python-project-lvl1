#!/usr/bin/env python3.10
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i <= number / 2:
        if number % i == 0:
            return False
        i += 1
    return True


def solution():
    question = random.randint(1, 100)
    if is_prime(question):
        correct_answer = 'yes'
        return question, correct_answer
    correct_answer = 'no'
    return question, correct_answer
