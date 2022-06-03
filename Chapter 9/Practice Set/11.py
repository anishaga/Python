import os

with open("E:/Python/Chapter 9/Practice Set/sample69.txt","r") as f:
    data1 = f.read()

with open("E:/Python/Chapter 9/Practice Set/renamedByPython.txt","w") as f:
    f.write(data1)

os.remove("E:/Python/Chapter 9/Practice Set/sample69.txt")