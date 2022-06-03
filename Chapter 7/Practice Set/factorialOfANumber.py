num = int(input("Enter Number: "))
factorial = 1

for i in range(num,1,-1):
    factorial = factorial * i

print(factorial)