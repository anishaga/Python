class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def getDetails(self):
        print(f"Name Of The Programmer is: {self.name}")
        print(f"Role Of The Programmer is: {self.role}")
        print(f"Salary Of The Programmer is: {self.salary}")
    

p1 = Programmer("Anish",2000000,"SDE2")
p2 = Programmer("Harry",1000000,"SDE1")
p3 = Programmer("Alka",20000,"Intern")

p1.getDetails()
p2.getDetails()
p3.getDetails()
