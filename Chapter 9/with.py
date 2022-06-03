with open("E:/Python/Chapter 9/another.txt","w") as f:
    f.write("Written A Text")

with open("E:/Python/Chapter 9/another.txt","r") as f:
    a = f.read()
    print(a)