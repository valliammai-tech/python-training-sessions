# From the given array that has any number of sub-lists, dict, nested dicts, find out all the positive integers and store them in an array.
# In case of dicts take both keys and values positive intergers. From the final array create an occurrence dictionary to figure out the occurrence of each number.
# inputs = [1,2,3,4,5,[True,False,-110.100,-200,500,[1,2,3,4,5]],{0:1,1:2,3:4,5:[10,True,-1100,200,300]}]
# output = [1,2,100,200,400,240,201,10,100,500,1,2,3,10,1,2,3,4,5,1,2]
# dict_output = {1:4,2:4,100:2,200:1,400:1,240:1,201:1,10:2,500:1,3:2,4:1,5:1}


# function similar of in-built set function

def set_func(uni):
    uniquevalues = []
    for i in uni:
        if i not in uniquevalues:
              uniquevalues.append(i)
    return uniquevalues


# Main Program

def flatten_func(inputs):
    flat=[]
    while inputs:
        element=inputs.pop()
        if type(element) == dict:
            for i,j in element.items():
                inputs.append(i)
                inputs.append(j)
        elif type(element) == list:
            inputs.extend(element)
        else:
            flat.append(element)  
    output=[x for x in flat if x>0 if type(x) != bool]
    uni=set_func(output)
    ans={}
    for i in uni:
        occ=0
        for j in output:
            if i==j:
                occ=occ+1
        ans[i]=occ
    return(ans)

list1=[1,2,3,4,5,[True,False,-110.100,-200,500,[1,2,3,4,5]],{0:1,1:2,3:4,5:[10,True,-1100,200,300]}]

flatten_func(list1)