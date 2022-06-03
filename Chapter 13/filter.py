def greaterThan5(num):
    if num > 5:
        return True
    else:
        return False


l = [1, 2, 3, 4, 5, 6, 7, 8, 1, 98]
print(list(filter(greaterThan5,l)))