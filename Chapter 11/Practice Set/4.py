class complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        if (self.b > 0):
            return f"{self.a} + i{self.b}"
        else:
            return f"{self.a} - i{self.b * -1}"

    def __add__(self,num2):
        return complex(self.a + num2.a, self.b + num2.b)

    def __mul__(self,num2):
        return complex((self.a * num2.a)-(self.b * num2.b), ((self.a * num2.b)+(self.b * num2.a)))

c1 = complex(1,4)
print(c1)

c2 = complex(8,5)
print(c2)

c3 = c1 + c2
print(c3)

c4 = c1 * c2
print(c4)