a = 69

def increment():
    global a
    print(a)
    a = a + 1
    return a

increment()
print(a)