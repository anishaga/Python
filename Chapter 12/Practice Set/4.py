def divis(num1,num2):
    try:
        print(num1/num2)
    except Exception as e:
        print("∞")

num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))

divis(num1,num2)