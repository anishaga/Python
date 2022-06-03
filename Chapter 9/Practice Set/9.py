with open("E:/Python/Chapter 9/Practice Set/donkeyFile.txt","r") as f:
    data1 = f.read()

with open("E:/Python/Chapter 9/Practice Set/donkeyCopy.txt","r") as f:
    data2 = f.read()

if data1 == data2:
    print("Identical Data")
else:
    print("Not Identical")
