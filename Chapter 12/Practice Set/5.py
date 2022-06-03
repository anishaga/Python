n = int(input("Enter Number: "))

a = [i*n for i in range(1,11)]


filename = "E:/Python/Chapter 12/Practice Set/tables.txt"
with open(filename,"w") as f:
    f.write(str(a))
