def square(num):
    return num*num

l1 = [1,2,4]

# #Method1
# l2 = []
# for i in l1:
#     l2.append(square(i))
# print(l2)

#Method2
print(list(map(square,l1)))
