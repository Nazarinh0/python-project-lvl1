import prompt
import random


def is_even(number: int) -> bool:
    """Check if given number is even."""
    return number % 2 == 0


def play_even():
    """Main logic of the Brain Even Game."""
    print(f'Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    score = 0
    goal = 3
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while True:
        number = random.randint(1, 100)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if is_even(number):
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


