with open("E:/Python/Chapter 9/Practice Set/donkeyFile.txt","r") as f:
    data = f.read()

with open("E:/Python/Chapter 9/Practice Set/donkeyCopy.txt","w") as f:
    f.write(data)