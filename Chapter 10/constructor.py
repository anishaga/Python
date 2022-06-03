# class Employee:
#     def __init__(self):
#         print("This statement gets printed automatically")

# emp1 = Employee()


class Employee:
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role  = role
        print("This statement gets printed automatically")
    
    def getDetails(self):
        print(f"Name is {self.name}")
        print(f"Role is {self.role}")
        print(f"Salary is {self.salary}")

emp1 = Employee("ABC",10000,"SDE")
emp1.getDetails()
