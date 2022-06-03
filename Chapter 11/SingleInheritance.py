class Employee:
    company = "INFY"
    def showDetails(self):
        print("Hello I Am An Employee")

class Programmer(Employee):
    def showDetails(self):
        print(f"Hello I Am A Programmer In {self.company} ")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()