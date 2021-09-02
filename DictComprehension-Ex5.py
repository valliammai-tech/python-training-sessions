# Question 3 -
#
# using Dict Comprehension find the occurrences of Numbers. Your function will take an Integer X followed by any
# number of Arrays. You need to parse each array and find out elements in the Array that is divisible by X and
# return the count of numbers that's divisible by X with its position.
#
# Example: func(5, [1,20,35,45,90],[100,20,30,45,60,75,90],[2,3,30,19,90,25,80],[5,6,9,10,15,25,30])
# Output: {0:4},{1:7},{2:4},{3:5}


def func3(div, **arrays):
    nos = 0
    for arr in arrays.values():
        iterr = 0
        for i in arr:
            if i % div == 0:
                iterr = iterr + 1
        print({nos: iterr})
        nos = nos + 1

func3(5, [1,20,35,45,90],[100,20,30,45,60,75,90],[2,3,30,19,90,25,80],[5,6,9,10,15,25,30])
