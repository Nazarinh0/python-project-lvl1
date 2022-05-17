#!/usr/bin/env python3.10
import random
from operator import add, mul, sub

DESCRIPTION = 'What is the result of the expression?'

operators = ((add, '+'), (mul, '*'), (sub, '-'))


def solution():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator, operation_sign = random.choice(operators)
    question = f'{number1} {operation_sign} {number2}'
    correct_answer = str(operator(number1, number2))
    return question, correct_answer
