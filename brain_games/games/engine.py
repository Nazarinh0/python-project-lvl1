#!/usr/bin/env python3.10
import prompt


def play(game):
    """Define Main logic of the Brain Even Game."""
    name = prompt.string('May I have your name? ')
    score = 0
    goal = 3
    print(f'Hello, {name}')
    print(game.DESCRIPTION)
    while True:
        (question, correct_answer) = game.solution()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".')
            print(f"""Let's try again, {name}!""")
            break
        if score == goal:
            print(f'Congratulations, {name}!')
            break
