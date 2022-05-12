import random


def is_even(number: int) -> bool:
    """Checks if given number is even."""
    return number % 2 == 0

def ask_question():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    x = random.randint(0, 100)
    if x % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print('Question: ' + str(x))
    answer = input('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print("""'yes' is wrong answer ;(. Correct answer was 'no'.
        Let's try again, Bill!""")
        return False


