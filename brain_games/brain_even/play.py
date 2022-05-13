import prompt, even


def welcome_user():
    """Greet user after start of the game."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def play_even():
    name = welcome_user()
    welcome_user()
    even.ask_question()

