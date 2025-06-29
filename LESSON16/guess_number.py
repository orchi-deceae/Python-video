from random import choice
import sys

def closure(name='user'):
    game_count = 0
    wins_count = 0
    def guess():
        nonlocal name
        nonlocal game_count
        nonlocal wins_count
        python_guess = choice('123')
        player_guess = input(f'\n{name}, guess which number i\'m thinking of... \n1, 2 or 3.\n\n')

        # python_number = int(python_guess)
        player_number = int(player_guess)

        if player_number < 1 or player_number > 3:
            print('\nError:\nNot an options\n')
            return guess()

        print(f'\n{name}, chose {player_guess}.')
        print(f'\npython, chose {python_guess}.')

        if player_guess == python_guess:
            print(f'\n\n{name}, you win\n')
            wins_count+=1
        else:
            print(f'\n\n{name}, you lose\n')

        game_count+=1

        print(f'\nGame count: {game_count}')
        print(f'\n{name}\'s wins: {wins_count}')
        print(f'\nYour winning percentage: {wins_count / game_count:.2%}')

        while True:
            again = input(f'\n\nPlay again, {name}?\n\nY for Yes or\nQ to Quit\n\n').lower()

            if again == 'y': return guess()
            elif again == 'q': 
                if __name__ != '__main__': return
                sys.exit('\nThank you for playing\nGood Bye!\n\n')
            else: print('\nError:\nNot an option')

    return guess

if __name__ == '__main__':
    import argparse

    value = argparse.ArgumentParser()

    value.add_argument(
        '-n', '--name', required=True,
        help='Type your name'
    )
    obj = value.parse_args()

    name = obj.name

    guess = closure(name.title())
    guess()

    # py LESSON16/guess_number.py -n 'sherlock'
