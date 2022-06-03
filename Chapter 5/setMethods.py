#Creating Empty Set
b = set()

#Adding Values
b.add(4)
b.add(5)
b.add(5)
b.add(5)
b.add(5)
b.add((4,5,6))

print(b)

#Length Of Set
print(len(b))

#Remove Element
b.remove(4)
print(b)

#Pop Element
b.pop()
print(b)

#Clear Set
b.clear()
print(b)
