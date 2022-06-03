def removeWord(string1,remove):
    string1 = string1.replace(remove,"")
    return string1.strip()

string1 = input("Enter Desired String: ")
remove = input("Enter Word To Be Removed: ")

print(removeWord(string1,remove))