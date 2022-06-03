# with open("E:/Python/Chapter 9/Practice Set/poem.txt","w") as f:
#     f.write('''Twinkle, twinkle, little star
# How I wonder what you are
# Up above the world so high
# Like a diamond in the sky
# Twinkle, twinkle, little star
# How I wonder what you are''')

with open("E:/Python/Chapter 9/Practice Set/poem.txt","r") as f:
    data = f.read()


if "twinkle" in data:
    print("Twinkle Is Present")
else:
    print("Twinkle Is Not Present")
    