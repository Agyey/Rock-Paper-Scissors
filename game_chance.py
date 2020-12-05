from random import randint

user = input()
options = ['rock', 'paper', 'scissors']
computer = options[randint(0, 2)]
if user == computer:
    print(f'There is a draw ({user})')
else:
    condition = {
        'rock': {
            'paper': 'loss',
            'scissors': 'win'
        },
        'scissors': {
            'rock': 'loss',
            'paper': 'win'
        },
        'paper': {
            'scissors': 'loss',
            'rock': 'win'
        }
    }
    situation = condition[user][computer]
    if situation == 'loss':
        print(f'Sorry, but the computer chose {computer}')
    elif situation == 'win':
        print(f'Well done. The computer chose {computer} and failed')

