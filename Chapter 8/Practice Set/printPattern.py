# def printPattern(n):
#     for i in range(n,0,-1):
#         print("*" * i, end="")
#         print(" "*(n-i))

def printPattern(n):
    for i in range(n):
        print("*" * (n-i))

n = int(input("Enter Number: "))

printPattern(n)