class Employee:
    company = "Bharat Gas"
    salary = 5500
    bonus = 600
    
    @property
    def totalSalary(self):
        return self.salary + self.bonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.bonus = val - self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = 6000
print(e.salary)
print(e.bonus)
