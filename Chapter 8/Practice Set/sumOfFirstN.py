def sumOf(n):
    if (n==0):
        return 0
    return sumOf(n-1) + n

number = int(input("Enter Number:" ))
print(sumOf(number))