myDict = {
    "fast": "In A Quick Manner",
    "anish": "A Coder",
    "marks": [1,2,5],
    "anotherdict": {"Man": "A Boy"}
}

# Print Keys Of Dictionary
print(list(myDict.keys()))

# Print Values Of Dictionary 
print(list(myDict.values()))

# Print The (key,value) For All The Contents Of Dictionary
print(list(myDict.items()))

# Update The Dictionary
updateDict = {
    "lovish": "Friend",
    "shubham": "Friend",
    "anish": "An Engineer"
}

myDict.update(updateDict)
print(list(myDict.items()))

# Get:

print(myDict.get('anish')) #Prints value corresponding to anish
print(myDict['anish']) #Prints value corresponding to anish

print(myDict.get('anish1')) #Returns None Since anish1 is not present in the dictionary
# print(myDict['anish1']) #Throws An Error