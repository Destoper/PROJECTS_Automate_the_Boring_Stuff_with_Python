import random


def ask():
    choice = ''
    while choice.lower() not in ('heads', 'tails'):        
        print('Enter heads or tails:')
        choice = input()
    return choice  

print('Guess the coin toss!')
guess = ask()   

toss = random.randint(0, 2) # 0 is tails, 1 is heads
toss = 'tails' if toss == 0 else 'heads'

if toss == guess.lower():
    print('You got it!')
else:
    print('\nNope! Guess again!')
    guess = ask()       
    if toss == guess.lower():
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')