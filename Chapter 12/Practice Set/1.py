def readFile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())

    except Exception as e:
        print(f"{filename} Is Not Found")


readFile("E:/Python/Chapter 12/Practice Set/1.txt")
readFile("E:/Python/Chapter 12/Practice Set/2.txt")
readFile("E:/Python/Chapter 12/Practice Set/3.txt")