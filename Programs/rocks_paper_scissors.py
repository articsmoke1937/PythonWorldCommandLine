import random
import University.globals as globals

def rocks_paper_scis(cname, pname, choice):
    print(f'\n{globals.border}')
    print("Rock, Paper Scissors")
    print(f'{globals.border} \n')
    while choice== 4 or choice==1:
        computer_choice = random.choice(['scissors', 'rock', 'paper'])
        user_choice = input('Do you want - rock, paper, or scissors?\n')
        print(globals.border)
        if computer_choice == user_choice:
            print(
                f'\n{cname} chose {computer_choice} so the game is a TIE')
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print(
                f'\n{cname} chose {computer_choice} so {pname} WINS')
        elif user_choice == 'paper' and computer_choice == 'rock':
            print(
                f'\n{cname} chose {computer_choice} so {pname} WINS')
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print(
                f'\n{globals.cname} chose {computer_choice} so {pname} WINS')
        else:
            print(
                f'\n{globals.cname} chose {computer_choice} so {pname} LOSES')
        print(globals.border)
        print(f'\n{pname}, would you like to play again?\n1. Yes \n2. No')
        choice = int(input(globals.prompt))
