myDict = {
    "Fast": "In A Quick Manner",
    "Anish": "A Coder",
    "Marks": [1,2,5],
    "Another Dict": {"Man": "A Boy"}
}

print(myDict['Fast'])
print(myDict['Marks'])

myDict['Marks'] = [10,20,30]
print(myDict['Marks'])

print(myDict['Another Dict'])
print(myDict['Another Dict']['Man'])
