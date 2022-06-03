data = True
i = 1
with open("E:/Python/Chapter 9/Practice Set/log.txt","r") as f:
    while(data):
        data = f.readline().lower()
        if "python" in data:
            print(i)
        i = i+1