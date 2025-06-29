import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playeragain = True

        playerchoice = input("\nEnter... \n1 for rock,\n2 for paper,\n3 for scissors:\n\n")

        if playerchoice not in ['1','2','3']:
            print('You must enter 1, 2 or 3.')
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return '🎈 You win!'
            elif player == 2 and computer == 1:
                player_wins += 1
                return '🎈 You win!'
            elif player == 2 and computer == 1:
                player_wins += 1
                return '🎈 You win!'
            elif player == computer:
                return "👍 Tie"
            else:
                python_wins += 1
                return '🐍 python wins'
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count+=1

        print(f'Game count: {game_count}\n')
        print(f'Player wins: {player_wins}\n')
        print(f'Python wins: {python_wins}\n')

        while True:
            playeragain = input('play again? \n\nY for yes or \nQ to Quit \n\n')
            if playeragain.lower() not in ['y','q']:continue
            else: break

        if playeragain.lower() == 'y': 
            return play_rps()
        if playeragain.lower() == 'q': 
            sys.exit('\nThank you for playing \nGood Bye')
    return play_rps

play = rps()
play()