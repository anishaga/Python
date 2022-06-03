with open("E:/Python/Chapter 9/Practice Set/donkeyFile.txt","r") as f:
    data = f.read()

l1 = ["donkey","bad","hate"]

for i in l1:
    data = data.replace(i, "#@&%#")

with open("E:/Python/Chapter 9/Practice Set/donkeyFile.txt","w") as f:
    f.write(data)