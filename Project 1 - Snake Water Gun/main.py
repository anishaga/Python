import random

def playGame(p1,p2):
    if(p1 == p2):
        print("Both Have Chosen The Same")
    elif (p1 == 1):
        if (p2 == 2):
            print("Computer Wins")
        elif (p2 == 3):
            print("Player Wins")
    elif (p1 == 2):
        if (p2 == 1):
            print("Player Wins")
        elif (p2 == 3):
            print("Computer Wins")
    elif (p1 == 3):
        if (p2 == 1):
            print("Computer Wins")
        elif (p2 == 2):
            print("Player Wins")  

p1 = random.randint(1,3)
p2 = input("Player's Turn- Choose- Snake(s) || Water(w) || Gun(g):\n")

if (p2 == "s"):
    p2 = 1
elif (p2 == "w"):
    p2 = 2
elif (p2 == "g"):
    p2 = 3

if (p1 == 1):
    a1 = "Snake"
elif (p1 == 2):
    a1 = "Water"
elif (p1 == 3):
    a1 = "Gun"

if (p2 == 1):
    a2 = "Snake"
elif (p2 == 2):
    a2 = "Water"
elif (p2 == 3):
    a2 = "Gun"

print("Computer Has Chosen:",a1,"\nPlayer Has Chosen:",a2)

playGame(p1,p2)
