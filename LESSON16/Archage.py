import guess_number
import rps
import sys

def selectGame_(name='user'):
    welcome = False
    while True:
        if welcome: print(f'\nWelcome back to the archade {name}, ')
        print(f'Please enter 1, 2 or x')
        game = input('\nPlease chose a game:\n1 = guess my number\n2 = rock paper scissors\nOr press \"x\" to exist the Arcade\n\n').lower()

        if game == '1':
            guess = guess_number.closure(name)
            guess()
        elif game == '2':
            rps_game = rps.closure(name)
            rps_game()
        elif game == 'x':
            sys.exit('\nGood Bye!\n')
        else:
            print('\nError:\nNot an option')
        welcome = True

if __name__ == '__main__':
    import argparse

    value = argparse.ArgumentParser()

    value.add_argument(
        '-n', '--name', required=True,
        help='Type your name'
    )

    obj = value.parse_args()

    name = obj.name

    selectGame_(name.title())

    # py LESSON16/Archage.py -n 'sherlock'

