import random

def RockPaperScissor(player):
    RPS = ['rock', 'paper', 'scissor']
    computer = random.choice(RPS)

    # Where the game happen
    if player == RPS[0] and computer == RPS[0]:
        print('DRAW!')
    elif player == RPS[1] and computer == RPS[1]:
        print('DRAW!')
    elif player == RPS[2] and computer == RPS[2]:
        print('DRAW!')
    elif player == RPS[0] and computer == RPS[1]:
        print('Computer wins!')
    elif player == RPS[1] and computer == RPS[0]:
        print('You wins!')
    elif player == RPS[2] and computer == RPS[0]:
        print('Computer wins!')
    elif player == RPS[0] and computer == RPS[2]:
        print('You wins!')
    elif player == RPS[1] and computer == RPS[2]:
        print('Computer wins!')
    elif player == RPS[2] and computer == RPS[1]:
        print('You wins!')
    elif player != RPS[0]:
        print("Invalid input!")

user = input("Enter rock, paper or scissor: ")
RockPaperScissor(user.lower())

