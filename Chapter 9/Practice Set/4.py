# with open("E:/Python/Chapter 9/Practice Set/donkeyFile.txt","w") as f:
#     f.write("Hello donkey, you are donkey. Donkey is bad,I hate donkey")


with open("E:/Python/Chapter 9/Practice Set/donkeyFile.txt","r") as f:
    data = f.read()


with open("E:/Python/Chapter 9/Practice Set/donkeyFile.txt","w") as f:
    f.write(data.replace("donkey", "#####"))


