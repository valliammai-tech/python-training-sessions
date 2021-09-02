# Write a program to update dictionary values using dict comprehensions. Your function will take 3 inputs, A dict, and Integer X and Integer Y. 
# Find keys whose values are greater than integer X and multiply them by Integer Y
# Example - func({1:3,10:20,3:4,5:60,10:90},x=50,y=10)
# Output - {5:600, 10:900}

def dict_upd(dict1,x,y):
    new_dict={}
    for i,j in dict1.items():
        if j>x and j>y:
            new_dict[i]=j*y
    print(new_dict)
    dict1.update(new_dict)
    print(dict1)
    return (new_dict,dict1)

dict1={1:3,10:20,3:4,5:60,10:90}
x=50
y=10

dict_upd(dict1,x,y)