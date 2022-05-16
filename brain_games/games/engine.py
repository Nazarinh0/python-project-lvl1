#!/usr/bin/env python3.10
import prompt
import random

from brain_games.games import even


def play(game):
    """Main logic of the Brain Even Game."""
    name = prompt.string('May I have your name? ')
    score = 0
    goal = 3
    print(f'Hello, {name}')
    print(game.DESCRIPTION)
    while True:
        number = random.randint(1, 100)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if even.is_even(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was {correct_answer}.""")
            print(f"""Let's try again, {name}!""")
            break
        if score == goal:
            print(f'Congratulations, {name}!')
            break
