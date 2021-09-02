# Function to find out ways to form a string from another string. Function will take 2 strings as inputs. 
# You must find out all possible ways by which you can form string A from string B.
# You must validate to ensure that the strings are Alpha-numeric only, it must contain only strings and numbers. No other types are allowed.
# The length of String B should be greater than string A. Character once used from string B must not be used again.
# Return the final output in dictionary format with indexes and values. Indexes represent the index value in String B that has occurrence of a char from String A
# Example -> func("abc","gcb xyzbc amnopq copnotab coscab")
# Expected output -> [{0:'a',2:'c',3:'b'},{8:'b',9:'c',11:'a'},{18:'c',24:'a',25:'b'},{27,'c',31:'a',32:'b'}]


#Sub function to get set of string along with its index

def func(s1,s2,n):
     dic11={}
     for i in s1:
         dic11[s2.index(i,n)]=i
     return(dic11)

#function to find length of input passed

def length_func(xi):
    leng=0
    for i in xi:
        leng=leng+1
    return leng


# Main Program

def main_fun(str1,str2):
    if all(x.isalpha() or x.isspace() for x in str1):
        print("Only alphabetical letters and spaces in str1: yes")
    else:
        return ('Program terminated')
    if all(y.isalpha() or y.isspace() for y in str2):
        print("Only alphabetical letters and spaces in str2: yes")
    else:
        return ("Program terminated")
    if length_func(str2) < length_func(str1):
	return ("Program terminated as length of string B is smaller than string A")
    try:
        t=str2.count(str1[0])
        dict1=func(str1,str2,0)
        lis=[dict1]
        dict2=func(str1,str2,max(dict1)+1)
        if length_func(lis)<t:
            lis.append(dict2)
        dict3=func(str1,str2,max(dict2)+1)
        if length_func(lis)<t:
            lis.append(dict3)
        dict4=func(str1,str2,max(dict3)+1)
        if length_func(lis)<t:
            lis.append(dict4)
    except ValueError:
        print('value error raised')
    else:
        print('success')
    finally:
        list1=[dict1,dict2,dict3,dict4]
    return list1

main_fun(str1,str2)