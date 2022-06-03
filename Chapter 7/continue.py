#With For Loop
print("Using For LOOP")
for i in range(10):
    if i==5:
        continue
    print(i)

print("Using While LOOP")
i=0
while i<10:
    if i==5:
        i = i+1
        continue
    print(i)
    i = i+1