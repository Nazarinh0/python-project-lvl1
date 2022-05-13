import random, prompt


def is_even(number: int) -> bool:
    """Check if given number is even."""
    return number % 2 == 0


def ask_question():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number = random.randint(1, 100)
    print('Question: ' + str(number))
    answer = prompt.string('Your answer: ')
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"""'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Bill!""")  # CHANGE BILL TO NAME
        return False


print(ask_question())
