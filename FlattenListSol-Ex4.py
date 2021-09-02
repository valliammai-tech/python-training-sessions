# Question 2)
#
# Using List Comprehension flatten a List. Your Function will take 2 Lists namely ListA and ListB.
# You need to pick elements from ListA which are divisible by at-least 2 elements in ListB.
# Note ListB must contain at-least 2 elements else dont process. Return the final list.
#
# Example: func([10,30,35,40,45,28,39,50,61,78],[2,5,10,20,50])
# Output:[10,30,40,50]

# Function for set operation

def set_func(uni):
    uniquevalues = []
    for i in uni:
        if i not in uniquevalues:
              uniquevalues.append(i)
    return uniquevalues


# Main Program

def func2(lsta, lstb):
    flattenList = [j for i in lstb for j in lsta if j % i == 0]
    return list(set_func(filter(lambda x: flattenList.count(x) > 2, flattenList)))
