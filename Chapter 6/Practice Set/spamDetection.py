a = input("Enter Comment!\n")

if ("make a lot of money" in a):
    flag = 1
elif ("buy now" in a):
    flag = 1
elif ("subscribe this" in a):
    flag = 1
elif ("click this" in a):
    flag = 1
else:
    flag = 0

if (flag == 0):
    print("Not Spam")
else:
    print("Spam")

