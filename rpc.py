# Simple program that takes user input and compares it with randomly generated input of computer(Rock, Paper and scissor game)
import random
def gameAlgo(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you =='p':
            return True
        else:
            return False
    elif comp == 'p':
        if you == 's':
            return True
        else:
            return False
    elif comp == 's':
        if you == 'r':
            return True
        else:
            return False
    

rand = random.randint(1,3)
if rand == 1:
    comp = 'r'
elif rand == 2:
    comp = 'p'
else:
    comp = 's'

you = input("Enter 'r' for rock, 'p' for paper and 's' for scissor ")
print(f"You have chosen {you}, computer have chose {comp}")
game = gameAlgo(comp, you)
if game is None:
    print("The game is tie.")
elif game is True:
    print("You have won the game.")
else:
    print("You have lost the game.")

