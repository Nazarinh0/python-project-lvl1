import prompt

'''that function greets user after start of the game'''
def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
