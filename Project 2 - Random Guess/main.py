import random

def takeInput():
    p = 0
    while (p > 100 or p <= 0):
        p = int(input("Kindly Enter Your Guess(Between 1 To 100 Only): "))
    
    return p


def guess(c,p):
    flag = 1
    count = 1

    while flag == 1:
        if c == p:
            print(f"You Guessed The Correct Number In {count} Tries")
            flag = 0
        elif c > p:
            print("Number Is Smaller, TRY AGAIN")
            p = takeInput()
            count = count + 1 
        else:
            print("Number Is Larger, TRY AGAIN")
            p = takeInput()
            count = count + 1 


c = random.randint(1,100)
p = takeInput()
guess(c,p)