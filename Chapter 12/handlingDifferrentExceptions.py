try:
    a = int(input("Enter A Number: "))
    c = 1/a
    print(c)
except ValueError as e:
    print(f"Invalid Input Dude!! {e}")
except ZeroDivisionError as e:
    print("Make Sure You Are Not Dividing By 0")
except Exception as e:
    print(f"Invalid Input: {e}")

print("Thanks For Using This Program")