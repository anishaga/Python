class Human:

    def __init__(self):
        print("Auto Statement From Human")

class Employee(Human):

    def __init__(self):
        super().__init__()
        print("Auto Statement From Employee")


class Programmer(Employee):

    def __init__(self):
        super().__init__()
        print("Auto Statement From Programmer")

p = Programmer()
