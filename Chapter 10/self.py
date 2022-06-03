class Employee:
    def getSalary(self):
        print(f"Salary Is: {self.salary}")

emp1 = Employee()
emp1.salary = 100
emp1.getSalary()