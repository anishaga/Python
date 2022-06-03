n =3

for i in range(n):
    if (i==0 or i== n-1):
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*")