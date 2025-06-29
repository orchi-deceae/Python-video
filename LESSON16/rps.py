from random import choice
import sys

def closure(name='user'):
    wins_count = 0
    game_count = 0
    def rps():
        nonlocal name
        nonlocal wins_count
        nonlocal game_count

        mve = {
            '1': 'Rock',
            '2': 'Paper',
            '3': 'Scissors'
        }

        python_mve = choice('123')
        player_mve = input(f"\n{name}, Please Enter... \n1 for rock,\n2 for paper,\n3 for scissors:\n\n")

        if player_mve not in ['1', '2', '3']:
            print('\nError:\nNot an option\n')
            rps()

        print(f'\n{name}, chose {mve[player_mve]}')
        print(f'python, chose {mve[python_mve]}\n')

        if player_mve == '1' and python_mve == '3':
            print(f'{name}, wins\n')
            wins_count+=1
        elif player_mve == '2' and python_mve == '1':
            print(f'{name}, wins\n')
            wins_count+=1
        elif player_mve == '3' and python_mve == '2':
            print(f'{name}, wins\n')
            wins_count+=1
        elif player_mve == python_mve:
            print(f'Tie\n')
        else:
            print(f'{name}, loses\n')

        game_count+=1

        print(f'Games played {game_count}')
        print(f'Games won {wins_count}')

        def playAgain_():
            nonlocal name
            again = input(f'\n{name}, would you like to play again?\n\nY for yes\nN for no\n\n').lower()

            if again not in ['y', 'n']: 
                print(f'\nError:\nNot an option\n')
                return playAgain_()
            return again
        
        again = playAgain_()
        if again == 'y': return rps()
        else: 
            if __name__ != '__main__': return
            sys.exit('\nThank you for playing\nGood Bye!\n\n')
    return rps


if __name__ == '__main__':
    import argparse

    value = argparse.ArgumentParser()

    value.add_argument(
        '-n', '--name', required=True,
        help='Type your name'
    )

    obj = value.parse_args()

    name = obj.name

    rps_game = closure(name.title())
    rps_game()

    # py LESSON16/rps.py -n 'sherlock'