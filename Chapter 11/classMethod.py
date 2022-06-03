class Employee:
    salary = 100

    def changeSalary(self,sal):
        self.salary = sal

    @classmethod
    def changeSalaryClass(cls,sal):
        cls.salary = sal

e = Employee()
e.changeSalary(69)
print(e.salary)
print(Employee.salary)

e.changeSalaryClass(69)
print(e.salary)
print(Employee.salary)