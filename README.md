# python-training-sessions

Exact question (rough version) for future reference

Write python function to find the powers of numbers. Each item in the Array must take the next element in the   
    array as it pow and return. 
    If any number is left-behind without next number, then it shall take the min number in the array as its pow.
    The max pow that can be taken is 5. If there is any item in the Array whose next number in the array is > 5,
    then pow will not apply and its value remains the same.

 

    Ensure to handle all types of exceptions. No built-ins.

 

    Example :
        func(10,3,50,1,20,3,8,2)
    Output :
        [100,50,8000,64]

 

    Example - left-behind without next number, then it shall take the min number in the array as its pow :
        func(10,3,50,2,20,3,8,2,100)
    Output :
        [100,2500,8000,64,10000]

 

    Example If there is any item in the Array whose next number in the array is > 5 :
        func(10,6,50,2,20,3,8,2,100)
    Output :
        [10,2500,8000,64,10000]

 


--------------------------------------------------------------------------------------------

 


From the given array that has any number of sub-lists, dict, nested dicts find out all the positive integers
    and store them in an array. In case of dicts take both keys & values positive integers.
    From the final array create an occurrence dictionary to figure out the occurrence of each number.
    Dont use any built-ins. Please remember the input array can have any levels of nested lists, sub-lists
    and nested dictionaries

 

    inputs=[1,2,3,4,5, [True,False,-110.100,-200,500, [1,2,3,4,5]], {0:1,1:2,3:4,5:[10,True,-1100,200,300]}]

 

    Output :
        Final Array is [1,2,100,200,400,240,201,10,100,500,1,2,3,10,1,2,3,4,5,1,2]
        Final Occurrence dict is {1: 4, 2: 4, 100: 2, 200: 1, 400: 1, 240: 1, 201: 1, 10: 2, 500: 1, 3: 2, 4: 1, 5: 1}

 


--------------------------------------------------------------------------------------------

 

Function to find out ways to form a string from another string. Function will take 2 strings as inputs.
    You must find out all possible ways by which you can form string A from String B.
    You must validate to ensure that the strings are Alpha-numeric only, it must contain
    only strings and numbers. 
    No other types are allowed. The length of String B must be >er than String A.
    Char once used from String B must not be used again.
    Return the final Output in dictionary format with indexes and values.
    Indexes represent the index value in String B that has occurrence of a char from String A.

 

    Function to find out ways to form a string from another string. Function will take 2 strings as inputs.

 

    Example :

 

      func("abc", "agcb xyzbc amnopq copnotab coscab")

 

      Figure out how to form string "abc" from "agcb xyzbc amnopq copnotab coscab"
      say StringA = "abc"
          StringB = "agcb xyzbc amnopq copnotab coscab"
          StringB[0]='a', StringB[2]='c', StringB[3]='b' -> Hence we can form 'abc' from char positions 0,2,3
          StringB[8]='b', StringB[9]='c', StringB[11]='a' -> Hence we can form 1 more 'abc' from char positions 8,9,11
          StringB[18]='c', StringB[24]='a', StringB[25]='b' -> Hence we can form 1 more 'abc' from char positions 18,24,25
          StringB[27]='c', StringB[31] ='a', StringB[32]='b'-> Hence we can form 1 more 'abc' from char positions 27,31,32

 

      So final Output is;

 

        [{0:'a', 2:'c', 3:'b'}, {8:'b', 9:'c', 11:'a'}, {18:'c', 24:'a', 25:'b'}, {27:'c', 31:'a', 32:'b'}]

 

--------------------------------------------------------------------------------------------

 

Using List comprehension flatten a List. Your Function will take 2 Lists namely ListA and List B. 
    You need to pick elements from ListA which are divisible by any element in ListB.
    Note ListB must contain atleast 2 elements else dont process.
    Return the final list.

 

    func([10,30,35,40,45,28,39,50,61,78],[2,5,10,20,50])
    Output: [10,30,40,50]
    Explanation:
      -> 10 is divisible by 2,5,10 in ListB
      -> 30 is divisible by 2,5,10 in ListB
      -> 40 is divisible by 5,10,20 in ListB
      -> 50 is divisible by 2,5,10,20,50 in ListB

 

--------------------------------------------------------------------------------------------

 


Using Dict Comprehension find the Occurences of Numbers. Your function will take an Integer X followed
    by any number of Arrays. You need to parse each array and find out elements in the Array that is divisible by X and
    return the count of numbers thats divisible by X with its position.

 

    Example:
      func(5, [1,20,35,45,90],[100,20,30,45,60,75,90],[2,3,30,19,90,25,80],[5,6,9,10,15,25,30])

 

    Output:
      {0:4, 1:7, 2:4, 3:5}

 

    Explanation:
      {0:4, 1:7, 2:4, 3:5}
        -> 0 th Array has 4 Elements divisible by X      
        -> 1 st Array has 7 Elements divisible by X
        -> 2 nd Array has 4 Elements divisible by X
        -> 3 rd Array has 5 Elements divisible by X

 

--------------------------------------------------------------------------------------------

 

Write a Program to update dictionary Values using dict comprehensions. 
    Your function will take 3 inputs, A dict, an Integet X and Interget Y.
    Find keys whose values are >er than Integer X and multiply them by Integer Y.

 

    Example:

 

      func({1:3,10:20,3:4,5:60,10:90},x=50,y=10)
    Output:
      {5:600, 10:900} -> Since keys 5 and 10 have values > 50

 

--------------------------------------------------------------------------------------------

 

Program to flatten a list using recursions. Input list can contain any levels of sub-lists

 

    Example: [1,2,3,4,5, [10,20,30,4,50,60,100],90,200,[300,10]]
    Output: 1,2,3,4,5,10,20,30,4,50,60,100,90,200,300,10

 


--------------------------------------------------------------------------------------------
