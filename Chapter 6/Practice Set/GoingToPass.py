m1 = int(input("Enter Marks: "))
m2 = int(input("Enter Marks: "))
m3 = int(input("Enter Marks: "))

if (m1 >= 33 or m2 >= 33 or m3 >= 33):
    totalPer = (m1+m2+m3)/3
    if (totalPer >= 40):
        print("You Are Passed")
    else:
        print("You Are Failed")
else:
    print("You Are Failed")