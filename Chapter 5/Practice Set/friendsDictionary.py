a = {}
n1 = input("Enter Name: ")
l1 = input("Enter Favourite Language: ")

n2 = input("Enter Name: ")
l2 = input("Enter Favourite Language: ")

n3 = input("Enter Name: ")
l3 = input("Enter Favourite Language: ")

n4 = input("Enter Name: ")
l4 = input("Enter Favourite Language: ")

b = {
    n1:l1,
    n2:l2,
    n3:l3,
    n4:l4
}

a.update(b)

print(a)