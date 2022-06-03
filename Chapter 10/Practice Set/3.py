class ClassAttribute():
    a = 100

obj = ClassAttribute()
obj.a = 0
print(obj.a)
print(ClassAttribute.a)