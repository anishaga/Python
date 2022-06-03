class Calculator:
    def __init__(self,num):
        self.num = num
    
    def square(self):
        print(self.num**2)
    
    def cube(self):
        print(self.num**3)

    def sqrt(self):
        print(self.num**0.5)

    @staticmethod
    def greet():
        print("Hello User")

# value1 = Calculator(10)
value1 = Calculator(4)
value3 = Calculator(9)

value1.greet()
value1.square()
value1.cube()
value1.sqrt()


