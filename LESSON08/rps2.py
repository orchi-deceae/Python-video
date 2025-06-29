import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playeragain = True

while playeragain:

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

    playerchoice = input("\nEnter... \n1 for rock,\n2 for paper,\n3 for scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit('You must enter 1, 2 or 3.')

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

    playeragain = input('play again? \nY for yes or \n Q to Quit \n\n')

    if playeragain.lower() == 'y': 
        continue
    if playeragain.lower() == 'q': 
        sys.exit('Thank you for playing \nGood Bye')
        # playeragain = False
        # break