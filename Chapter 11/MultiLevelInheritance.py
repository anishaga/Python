class Human:
    place = "Earth"

    def about(self):
        print(f"Hey, there I am a human and i live at {self.place}")

class Employee(Human):
    company = "Metaverse"
    place = "Silicon Valley"
    def about(self):
        print(f"Hey, there I work at {self.company} and i live in {self.place}")

class Programmer(Employee):
    role = "SDE"
    def about(self):
        print(f"Hey, there I am a {self.role} at {self.company} and i live in {self.place}")

h = Human()
e = Employee()
p = Programmer()

h.about()
e.about()
p.about()