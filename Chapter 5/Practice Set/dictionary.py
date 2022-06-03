hindiDict = {
    "Gaadi":"Car",
    "Laathi":"Stick",
    "Kitaab":"Book",
    "Balti":"Bucket"
}

print("Options Are: ", list(hindiDict.keys()))
a = input("Enter Hindi Word Whose Translation You Need: ")

print("English Translation Is: ", hindiDict.get(a))