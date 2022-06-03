def factorial(num):
    if (num <= 1):
        return 1

    return factorial(num-1)*num

num1 = int(input("Enter Number: "))

print(factorial(num1))