import prompt


def welcome_user():
    """Greet user after start of the game."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
