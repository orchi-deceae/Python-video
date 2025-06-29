import sys
import random
from enum import Enum
import argparse

# ver = argparse.ArgumentParser(
#     description='test'
# )
# ver.add_argument(
#     '-r', '--rps', metavar='rock_paper_scissors',
#     required=True, help='put number', 
#     choices=['1', '2', '3']
# )
# print(ver)
# v = ver.parse_args()
# print(v.rps)

def rps(name='user'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playeragain = True

        playerchoice = input(f"\n{name}, Please Enter... \n1 for rock,\n2 for paper,\n3 for scissors:\n\n")

        if playerchoice not in ['1','2','3']:
            print(f'{name} please enter 1, 2 or 3.')
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f'🎈{name}, You win!'
            elif player == 2 and computer == 1:
                player_wins += 1
                return f'🎈{name}, You win!'
            elif player == 2 and computer == 1:
                player_wins += 1
                return f'🎈{name}, You win!'
            elif player == computer:
                return f"👍{name},  Tie"
            else:
                python_wins += 1
                return '🐍 python wins\nSorry {name}'
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count+=1

        print(f'Game count: {game_count}\n')
        print(f'{name} wins: {player_wins}\n')
        print(f'Python wins: {python_wins}\n')

        while True:
            playeragain = input(f'play again, {name}? \n\nY for yes or \nQ to Quit \n\n')
            if playeragain.lower() not in ['y','q']:continue
            else: break

        if playeragain.lower() == 'y': 
            return play_rps()
        if playeragain.lower() == 'q': 
            sys.exit(f'\nThank you for playing \nGood Bye {name}')
    return play_rps


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    
    args = parser.parse_args()

    # hello(args.name, args.lang)
    
    rock_paper_scissors = rps(args.name.title())
    rock_paper_scissors()
