while (True):
    print("Press 'q' to quit")
    a = input("Enter A Number: ")
    if (a == 'q'):
        print("**** Thanks A Playing ****")
        print("     Have A Nice Day")
        break
    try:
        a = int(a)
        if a > 6:
            print("You Enter A Number Greater Than 6")
    except Exception as e:
        print(f"Invalid Input, Error Code: {e}")
        print("\t\t***TRY AGAIN***")