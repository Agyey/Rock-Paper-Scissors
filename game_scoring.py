from random import randint
import os

# Take Users Name
name = input('Enter your name: ')
print(f'Hello, {name}')
current_score = 0
with open('rating.txt', 'r') as f:
    while True:
        line = f.readline()
        if line:
            user, score = line.strip().split()
            if user == name:
                current_score = int(score)
                break
        else:
            break

# Run game till users Says '!exit'
while True:
    user = input()
    # Valid Options
    options = ['rock', 'paper', 'scissors']
    # Randomly Select Computer's choice
    computer = options[randint(0, 2)]
    if user == '!exit':
        print('!bye')
        break
    elif user == '!rating':
        print(f'Your rating: {current_score}')
    elif user in options:
        if user == computer:
            print(f'There is a draw ({user})')
            current_score += 50
        else:
            # Condition, first condition vs second result
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
                current_score += 100
                print(f'Well done. The computer chose {computer} and failed')
    else:
        print('Invalid input')
