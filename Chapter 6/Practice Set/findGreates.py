n1 = int(input("Enter Number: "))
n2 = int(input("Enter Number: "))
n3 = int(input("Enter Number: "))
n4 = int(input("Enter Number: "))

if (n1 > n2):
    if(n3 > n4):
        if (n1 > n3):
            print(n1, "Is Greatest")
        else:
            print(n3, "Is Greatest")
    else:
        if (n1 > n4):
            print(n1, "Is Greatest")
        else:
            print(n4, "Is Greatest")
else:
    if(n3 > n4):
        if (n2 > n3):
            print(n2, "Is Greatest")
        else:
            print(n3, "Is Greatest")
    else:
        if (n2 > n4):
            print(n2, "Is Greatest")
        else:
            print(n4, "Is Greatest")
