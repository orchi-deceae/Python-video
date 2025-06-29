import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playeragain = True


    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

    playerchoice = input("\nEnter... \n1 for rock,\n2 for paper,\n3 for scissors:\n\n")

    if playerchoice not in ['1','2','3']:
        print('You must enter 1, 2 or 3.')
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")


    if player == 1 and computer == 3:
        print('🎈 You win!')
    elif player == 2 and computer == 1:
        print('🎈 You win!')
    elif player == 2 and computer == 1:
        print('🎈 You win!')
    elif player == computer:
        print("👍 Tie")
    else:
        print('🐍 python wins')

    while True:
        playeragain = input('play again? \nY for yes or \n Q to Quit \n\n')
        if playeragain.lower() not in ['y','q']:continue
        else: break

    if playeragain.lower() == 'y': 
        return play_rps()
    if playeragain.lower() == 'q': 
        sys.exit('\nThank you for playing \nGood Bye')
play_rps()