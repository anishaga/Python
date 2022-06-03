from functools import reduce    

def findMax(a,b):
    if (a>b):
        return a
    else:
        return b

l = [43,24,1,45,10,69,13,53,17]

val = reduce(findMax,l)
print(val)