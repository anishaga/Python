class twoD:
    def __init__(self,num1,num2):
        self.i = num1
        self.j = num2

    def __str__(self):
        return f"{self.i}i + {self.j}j"

class threeD(twoD):

    def __init__(self,num1,num2,num3):
        super().__init__(num1,num2)
        self.k = num3

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

t = twoD(1,2)
print(t)

d = threeD(1,2,3)
print(d)