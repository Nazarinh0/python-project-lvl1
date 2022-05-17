#!/usr/bin/env python3.10
import random

DESCRIPTION = 'What number is missing in the progression?'


def get_progression():
    start = random.randint(1, 20)
    stop = random.randint(50, 100)
    step = random.randint(3, 7)
    return list(range(start, stop, step))


def solution():
    progression = get_progression()
    correct_answer = str(random.choice(progression))
    progression = ' '.join(str(i) for i in progression)
    question = progression.replace(correct_answer, "..")
    return question, correct_answer
