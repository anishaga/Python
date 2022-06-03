def printTable(n):
    for i in range(1,n+1):
        print(n,"*",i,"=",n*i)

n = int(input("Enter Number: "))
printTable(n)