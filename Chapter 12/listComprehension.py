a = [3,6,7,13,43,67,41,76,58,35,84,65,97,96,64]
# b=[]

# for item in a:
#     if item%2 == 0:
#         b.append(item)

# print(b)

b = [i for i in a if i%2==0]
print(b)
