word = "once upon a time there was a boy named Anish"

#String Functions

#Length
print(len(word))

#Ends With (BOOL)
print(word.endswith("named"))
print(word.endswith("Anish"))

#Count
print(word.count("A"))

#Capitalize (First Word Is Capitalized)
print(word.capitalize())

#Find (Returns The Index If Found || Else Gives -1)
print(word.find("boy"))

#Replace
print(word.replace("Anish", "Anuj"))
