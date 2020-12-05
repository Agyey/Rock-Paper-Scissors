from random import randint
import os

def result(first, second, options):
    i = options.index(first)
    all = options[i+1:] + options[:i]
    l = len(all)
    wins = all[:l//2]
    if second not in wins:
        return 'win'
    else:
        return 'loss'
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
user_options = input().strip()
if user_options:
    options = user_options.split(',')
else:
    options = ['rock', 'paper', 'scissors']
print("Okay, let's start")
# Run game till users Says '!exit'
while True:
    user = input()
    # Randomly Select Computer's choice
    computer = options[randint(0, len(options)-1)]
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
            if result(user, computer, options) == 'loss':
                print(f'Sorry, but the computer chose {computer}')
            elif result(user, computer, options) == 'win':
                current_score += 100
                print(f'Well done. The computer chose {computer} and failed')
    else:
        print('Invalid input')
