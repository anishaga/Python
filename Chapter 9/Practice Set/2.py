with open("E:/Python/Chapter 9/Practice Set/highScore.txt","r") as f:
    data = f.read()

score = 70

if (len(data) == 0 or int(data) < score):
    with open("E:/Python/Chapter 9/Practice Set/highScore.txt","w") as f:
        temp = str(score)
        f.write(temp)
