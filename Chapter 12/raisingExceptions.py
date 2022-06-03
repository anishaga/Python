def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This Is Not Good")

a = increment('a10')
print (a)