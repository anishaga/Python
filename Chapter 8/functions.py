def sum(marks):
    totalSum = 0
    for i in marks:
        totalSum = totalSum + i
    return totalSum

def percentage(marks):
    return sum(marks)/len(marks)

marks1 = [45,78,86,77]
percent1 = percentage(marks1)
print(percent1)

marks2 = [99,99,99,99,99,99,99,99,99,99,99,99,99,99]
percent2 = percentage(marks2)
print(percent2)