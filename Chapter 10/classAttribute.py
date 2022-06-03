class Employee:
    company = "Google"

anish = Employee()
arjun = Employee()

print(anish.company)
print(arjun.company)

Employee.company = "Facebook"
print(arjun.company)
print(anish.company)