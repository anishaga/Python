try:
    i = int(input("Enter Number: "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("Successfully Executed Try Statement")