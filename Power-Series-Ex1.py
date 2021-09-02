# Write python function to find the powers of numbers. Each item in the Array must take the next element in the array as its pow and return.
# If any number is left-behind without next number, then it shall take the min number in the array as its pow. The max pow that can be taken is 5.
# If there is any item in the Array whose next number in the array is greater than 5, then pow will not apply and its value remains the same.
# Example i) function(10,3,50,1,20,3,8,2)  => output = [100,50,8000,64]
# Example ii) function(10,3,50,2,20,3,8,2,100) => output = [100,2500,8000,64,10000]
# Example iii) function(10,6,50,2,20,3,8,2,100) => output = [10,2500,8000,64,10000]


#function to find length of input passed

def length_func(xi):
    leng=0
    for i in xi:
        leng=leng+1
    return leng
	
#function to find minimum value of input passed

def min_func(mi):
    v_min = mi[0];  
    for i in range(0, length_func(mi)):
        if(mi[i] < v_min):
            v_min = mi[i];   
    return(v_min)


# Main Program to generate power of numbers

def function(*x):
    powers_upd=[]
    powers=[j for i,j in enumerate(x) if i%2!=0]
    numbers=[j for i,j in enumerate(x) if i%2==0]
    if length_func(numbers)!=length_func(powers):
        powers.append(min_func(x))
    for i in powers:
        if i > 5:
            powers_upd.append(1)
        else:
            powers_upd.append(i)
    if powers==powers_upd:
        output_value=[x**y for x,y in zip(numbers,powers)]
    else:
        output_value=[x**y for x,y in zip(numbers,powers_upd)]
    return output_value

function(10,3,50,1,20,3,8,2)
function(10,3,50,2,20,3,8,2,100)
function(10,6,50,2,20,3,8,2,100)