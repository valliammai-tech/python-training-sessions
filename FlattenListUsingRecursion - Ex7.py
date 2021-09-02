# Program to flatten a list using recursions. Input list can contain any levels of sub-lists
# Example - func([1,2,3,4,5,[10,20,30,4,50,60,100],90,200,[300,10]])
# Output - [1,2,3,4,5,10,20,30,4,50,60,100,90,200,300,10]

def recur_flatten_list(list1):
    if len(list1)==1:
        if type(list1[0]) == list:
            result =  recur_flatten_list(list1[0])
        else:
            result=list1
    elif type(list1[0])==list:
        result = recur_flatten_list(list1[0])+recur_flatten_list(list1[1:])
    else:
        result=[list1[0]]+recur_flatten_list(list1[1:])
    return result

list1=[1,2,3,4,5,[10,20,30,4,50,60,100],90,200,[300,10]]

recur_flatten_list(list1)