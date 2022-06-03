class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        return self.num + num2.num
    
    def __mul__(self,num2):
        return self.num * num2.num

n1 = Number(2)
n2 = Number(4)

n3 = n1 + n2
n4 = n1 * n2

print(n3)
print(n4)
