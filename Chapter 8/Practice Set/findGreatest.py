def findGreatest(n1,n2,n3):
    if (n1 > n2):
        if (n1 > n3):
            return n1
        else:
            return n3
    else:
        if (n2 > n3):
            return n2
        else:
            return n3

n1 = int(input("Enter Number: "))
n2 = int(input("Enter Number: "))
n3 = int(input("Enter Number: "))

print("Largest Number Is:",findGreatest(n1,n2,n3))