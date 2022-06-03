n = int(input("Enter Number: "))
n=10
for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1))

# n= 10
# for i in range(n):
#     print(" "*(n-i+10),end="")
#     print(2**n,end="")
#     print(" "*(n+i),end="")
#     if n==0:
#         continue
#     else:
#         print(2**n)
#     n= n-1
