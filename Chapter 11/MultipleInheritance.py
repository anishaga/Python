class Employee:
    company = "INFY"
    level = 0

class FreeLancer:
    company = "Brave Inc."
    level = 1

    def levelUp(self):
        self.level = self.level + 1

class Programmer(Employee, FreeLancer):
    work = "Programming"


p = Programmer()
print(p.company)
print(p.level)
p.levelUp()
print(p.level)

