import random

def game(comp,mine):
    if (comp==mine):
        return None
    if (comp=="rock" and mine=="paper"):
        return True
    elif(comp=="scisor" and mine=="rock"):
        return True
    elif(comp=="paper" and mine=="scissor"):
        return True
    else:
        return False        


choice = ("rock","paper","scisor")
comp = random.randint(0,2)
comp = choice[comp]
mine = input("choose either rock ,paper,and scisor: ")
win = game(comp,mine)
print("You choose",mine ,"and the computer choose",comp)
if win is None:
    print("Match Drawn")
if win:
    print("you won")
else:
    print("you lose")   
