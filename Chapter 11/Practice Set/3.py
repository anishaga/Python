class Employee:
    salary = 1000
    increment = 150

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,val):
        self.increment = val - self.salary

e = Employee()
print (e.salaryAfterIncrement)
e.salaryAfterIncrement = 5000
print(e.salary)
print(e.increment)