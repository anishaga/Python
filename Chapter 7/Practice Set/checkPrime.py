num = int(input("Enter Number: "))
i = num-1
while i > 1:
    if(num % i == 0):
        print("Not Prime")
        break
    i = i-1
else:
    print("Prime Number")