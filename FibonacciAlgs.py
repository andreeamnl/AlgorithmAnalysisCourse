import matplotlib.pyplot as plt
from time import process_time
import numpy as np
from numpy.linalg import matrix_power
import math


input_array1=np.array([5,7,10,12,15,17,20,22,25,27,30,32,35,37,40,45])
input_array2=np.array([501,631,794,1000,1259,1585,1995,2512,3162,3981,5012,6310,7943,10000,12589])



################################################
#######matrix method

def fibmat(n):
    i = np.array([[0, 1], [1, 1]])
    return np.matmul(matrix_power(i, n), np.array([1, 0]))[1]


def fib(n):
    if n%2 != 0:#even
        return fib_odd(n)
    return fib_even(n)

def fib_odd(N):
    n = int((N+1)/2)
    Fn = fibmat(n) 
    Fn1 = fibmat(n-1)
    return Fn1**2 + Fn**2

def fib_even(N):
    n = int(N/2)
    Fn = fibmat(n) 
    Fn1 = fibmat(n-1)
    return Fn * (2*Fn1 + Fn)


def y_vals(element):
    start=process_time()
    fib(element)
    end=process_time()
    return end-start



y_new= np.array([])
y_new1= np.array([])



for i in input_array1:
    y_new= np.append(y_new, y_vals(i))
print("###################################")


for i in input_array2:
    y_new1= np.append(y_new1, y_vals(i))
print("###################################")




##plotting for matrix method, first set of numbers
plt.figure(figsize=(8,8))    
plt.grid()
plt.plot(input_array1,y_new, 'r--', color='orange', linewidth=3)
plt.title('Double Fibonacci Matrix Exponentiation (1st set)')
plt.ylabel('Time(s)')
plt.xlabel("n-th Fibonacci Term")
plt.show()


##plotting for matrix method, second set of numbers
plt.figure(figsize=(8,8))    
plt.grid()
plt.plot(input_array2,y_new1, 'r--', color='red', linewidth=3)
plt.title('Double Fibonacci Matrix Exponentiation (2nd set)')
plt.ylabel('Time(s)')
plt.xlabel("n-th Fibonacci Term")
plt.show()




################################################

#######textbook fibonacci recursion
def fib_it(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_it(n-1) + fib_it(n-2)


def y_vals_it(element):
    start=process_time()
    fib_it(element)
    end=process_time()
    return end-start


y_new2= np.array([])


#!!! this code takes a while to run
for i in input_array1:
    y_new2= np.append(y_new2, y_vals_it(i))
print("###################################")


##plotting for recursive method, first set of numbers
plt.figure(figsize=(8,8))    
plt.grid()
plt.plot(input_array1,y_new2,'r--', color='orange', linewidth=3)
plt.title('Textbook Recursion Method (1st set)')
plt.ylabel('Time(s)')
plt.xlabel("n-th Fibonacci Term")
plt.show()


##plotting for recursion method, second set of numbers
##Actually, we shouldn't do this





################################################
#######Dynamic Programming

## new/old method
def fib_d(n):
    new, old = 1, 0
    for i in range(n):
            new, old = old, new + old
    return old

y_new3= np.array([])
y_new4= np.array([])



##function that calculates elapsed time 
def y_vals3(element):
    start=process_time()
    fib_d(element)
    end=process_time()
    return end-start


##storing elapsed time for 1st set in an array
for i in input_array1:
    y_new3= np.append(y_new3, y_vals3(i))
print("###################################")

##storing elapsed time for 2nd set in an array
for i in input_array2:
    y_new4= np.append(y_new4, y_vals(i))
print("###################################")


##plotting for Dynamic Programming  new/old method, first set of numbers
plt.figure(figsize=(8,8))    
plt.grid()
plt.plot(input_array1,y_new3,'r--', color='orange', linewidth=3)
plt.title('Dynamic Programming new/old approach (1st set)')
plt.ylabel('Time(s)')
plt.xlabel("n-th Fibonacci Term")
plt.show()


##plotting for Dynamic Programming new/old method, second set of numbers
plt.figure(figsize=(8,8))    
plt.grid()
plt.plot(input_array2,y_new4, 'r--', color='red', linewidth=3)
plt.title('Dynamic Programming new/old approach (2nd set)')
plt.ylabel('Time(s)')
plt.xlabel("n-th Fibonacci Term")
plt.show()




########Memoized solution

y_new5= np.array([])
y_new6= np.array([])




def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if ((n==1) or (n==2)):
        result=1
    else:
        result= fib_2(n-1,memo)+fib_2(n-2,memo)
    memo[n]=result
    return result

def fib_memo(n):
    memo=[None]*(n+1)
    return fib_2(n,memo)

def y_vals4(element):
    start=process_time()
    fib_memo(element)
    end=process_time()
    return end-start


##storing elapsed time for 1st set in an array
for i in input_array1:
    y_new5= np.append(y_new5, y_vals4(i))
print("###################################")



###the following code gives us an error
##storing elapsed time for 2nd set in an array
#for i in input_array2:
#    y_new6= np.append(y_new6, y_vals4(i))
#print("###################################")
#print(y_new6)


##plotting for Dynamic Programming memoized solution method, first set of numbers
plt.figure(figsize=(8,8))    
plt.grid()
plt.plot(input_array1,y_new5,'r--', color='orange', linewidth=3)
plt.title('Dynamic Programming memo approach (1st set)')
plt.ylabel('Time(s)')
plt.xlabel("n-th Fibonacci Term")
plt.show()



#####bottom up approach
y_new7= np.array([])
y_new8= np.array([])


def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

def y_vals5(element):
    start=process_time()
    fib_bottom_up(element)
    end=process_time()
    return end-start


##storing elapsed time for 1st set in an array
for i in input_array1:
    y_new7= np.append(y_new7, y_vals5(i))
print("###################################")

##storing elapsed time for 2nd set in an array
for i in input_array2:
    y_new8= np.append(y_new8, y_vals5(i))
print("###################################")

##plotting for Dynamic Programming bottom-up solution method, first set of numbers
plt.figure(figsize=(8,8))    
plt.grid()
plt.plot(input_array1,y_new7,'r--', color='orange', linewidth=3)
plt.title('Dynamic Programming bottom-up approach (1st set)')
plt.ylabel('Time(s)')
plt.xlabel("n-th Fibonacci Term")
plt.show()


##plotting for Dynamic Programming bottom-up solution method, second set of numbers
plt.figure(figsize=(8,8))    
plt.grid()
plt.plot(input_array2,y_new8,'r--', color='red', linewidth=3)
plt.title('Dynamic Programming bottom-up approach (2nd set)')
plt.ylabel('Time(s)')
plt.xlabel("n-th Fibonacci Term")
plt.show()



################################
########binet's formula


y_new9= np.array([])
y_new10= np.array([])

def binets_formula(n):


    # splitting of terms for easiness
    sqrtFive = np.sqrt(5)
    alpha = (1 + sqrtFive) / 2
    beta = (1 - sqrtFive) / 2
    
    # Implementation of formula
    # np.rint is used for rounding off to integer
    Fn = np.rint(((alpha ** n) - (beta ** n)) / (sqrtFive))

    return Fn

def y_vals6(element):
    start=process_time()
    binets_formula(element)
    end=process_time()
    return end-start

##storing elapsed time for 1st set in an array
for i in input_array1:
    y_new9= np.append(y_new9, y_vals6(i))
print("###################################")

##storing elapsed time for 2nd set in an array
for i in input_array2:
    y_new10= np.append(y_new10, y_vals6(i))
print("###################################")


##plotting for Binet's solution method, first set of numbers
plt.figure(figsize=(8,8))    
plt.grid()
plt.plot(input_array1,y_new9,'r--', color='orange', linewidth=3)
plt.title('Binets approach (1st set)')
plt.ylabel('Time(s)')
plt.xlabel("n-th Fibonacci Term")
plt.show()


##plotting for Binet's solution method, second set of numbers
plt.figure(figsize=(8,8))    
plt.grid()
plt.plot(input_array2,y_new10,'r--', color='red', linewidth=3)
plt.title('Binets approach (2nd set)')
plt.ylabel('Time(s)')
plt.xlabel("n-th Fibonacci Term")
plt.show()



##########################################
####table output 1st set
print('Table time output')
print('[0]     5     7      10     12    15    17    20    22    25    27    30    32    35    37    40')
print('[1]',end='     ')
for i in y_new:
    print(round(i,4),end='   ')
print('\n')
print('[2]',end='    ')
for i in y_new2:
    print(round(i,3),end='  ')
print('\n')
print('[3]',end='     ')

for i in y_new3:
    print(round(i,4),end='   ')
print('\n')   
print('[4]',end='    ')

for i in y_new5:
    print(round(i,4),end='   ')
print('\n') 
print('[5]',end='     ')

for i in y_new7:
    print(round(i,4),end='   ')
print('\n')   
print('[6]',end='    ')

for i in y_new9:
    print(round(i,4),end='   ')
print('\n')   


##########################################
####table output 2nd set
print('Table time output  2nd set')
print('[0]     501  631  794  1000  1259  1585  1995  2512   3162   3981   5012  6310  7943  10000  12589')
print('[1]',end='     ')
for i in y_new1:
    print(round(i,4),end='   ')
print('\n')
print('[2]',end='    ')
for i in y_new4:
    print(round(i,3),end='   ')
print('\n')
print('[3]',end='   ')

for i in y_new8:
    print(round(i,4),end='  ')
print('\n')   
print('[4]',end='   ')

for i in y_new10:
    print(round(i,4),end='   ')
print('\n') 




##########################
#####comparison plots
plt.figure(figsize=(10,10))
plt.grid()
plt.plot(input_array2, y_new1,'g--', color='magenta', label='Double Fibonacci Matrix Exponentiation')
plt.plot(input_array2, y_new4, color='blue', label='Dynamic Programming new/old approach')
#plt.plot(input_array2, y_new8, color='yellow', label='Dynamic Programming bottom-up approach ')
plt.plot(input_array2, y_new10, color='green', label='Binets approach')
plt.title('2nd set Ultimate test')
plt.legend()
plt.show()

