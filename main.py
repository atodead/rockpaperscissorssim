import random

comp_wins = 0
player_wins = 0

print('ROCK PAPER SCISSORS BY ANIKETH SHET AKA ATODEAD')
def chooseopt():
    user = input('Choose rock, paper or scissors: ')
    if user in ['Rock', 'rock', 'r', 'R']:
        user = 'r'
    elif user in ['Paper', 'paper', 'p', 'P']:
        user = 'p'
    elif user in ['Scissors', 'scissors', 's', 'S']:
        user = 's'
    else:
        print("I don't understand, try again.")
        chooseopt()
    return user


def computeropt():
    computerchoice = random.randint(1, 3)
    if computerchoice == 1:
        computerchoice = 'r'
    elif computerchoice == 2:
        computerchoice = 'p'
    else:
        computerchoice = 's'
    return computerchoice


while True:
    print('')

    user = chooseopt()
    computerchoice = computeropt()

    print('')

    if user == 'r':
        if computerchoice == 'r':
            print('You chose rock. The computer chose rock. You tied.')

        elif computerchoice == 'p':
            print('You chose rock. The computer chose paper. You lose.')
            comp_wins += 1

        elif computerchoice == 's':
            print('You chose rock. The computer chose scissors. You win.')
            player_wins += 1

    elif user == 'p':
        if computerchoice == 'r':
            print('You chose paper. The computer chose rock. You win.')
            player_wins += 1

        elif computerchoice == 'p':
            print('You chose paper. The computer chose paper. You tied.')


        elif computerchoice == 's':
            print('You chose paper. The computer chose scissors. You lose.')
            comp_wins += 1

    elif user == 's':
        if computerchoice == 'r':
            print('You chose scissors. The computer chose rock. You lose.')
            comp_wins += 1

        elif computerchoice == 'p':
            print('You chose scissors. The computer chose paper. You win.')
            player_wins += 1

        elif computerchoice == 's':
            print('You chose scissors. The computer chose scissors. You tied.')

    print('')
    print('Player wins: ' + str(player_wins))
    print('Computer wins: ' + str(comp_wins))
    print('')

    user = input('Do you want to play again? (y/n)')
    if user in ['Y', 'y', 'yes', 'Yes']:
        pass
    elif user in ['N', 'n', 'no', 'No']:
        break
    else:
        break
