# In Python we can return multiple values from a functions at a time.
# Exmaple:-

def calc(a,b):
    sum1=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum1,sub,mul,div
w,x,y,z=calc(100,50)
print(w)
print(x)
print(y)
print(z)
# or we can store the retun values in tuple ,then we can print it as below.
t=calc(100,50)
for x in t:
    print(x)

# calc(100,b=50) valid
# calc(b=50,100) error 
# calc(50,a=100)  error ,calc() got multiple values for argument 'a'

def wish(name='guest',msg):pass # not valid
# error as below
SyntaxError: non-default argument follows default argument
  
def wish(msg,name='guest'):pass # Valid


# Variable lenght arguments method 
#----------------------------------------------------------------------------------
def sum(*n):  # this is the declaration 
  
# Example:-
def f1(*n):
    print("Var-arg functions")
    
f1()
f1(10)
f1(10,20)
f1(10,20,30,40)

# o/p:-
Var-arg functions
Var-arg functions
Var-arg functions
Var-arg functions

#Example:-

def f1(*n):    # here n become tuple and it store all values
    result=0
    for x in n:
        result=result+x
    print('the sum is',result)
    
f1()
f1(10)
f1(10,20)
f1(10,20,30,40)

# o/p:-
the sum is 0
the sum is 10
the sum is 30
the sum is 100

# Example:-

def f1(name,*n):
    result=0
    for x in n:
        result=result+x
    print('the sum is',name,result)
    
f1('ram')
f1('shayam',10)
f1('rr',10,20)
f1('rttt',10,20,30,40)
    
# o/p:-
the sum is ram 0
the sum is shayam 10
the sum is rr 30
the sum is rttt 100

# Example:- if we chnages the arguments

def f1(*n,name):
    result=0
    for x in n:
        result=result+x
    print('the sum is',name,result)
    
f1(name="ram")
f1(10,name="shayam")

#  o/p:-
the sum is ram 0
the sum is shayam 10

# Keyword variable lenght arguments:-
#-----------------------------------------------------------------------------------

#Example:-
def display(**kwargs): # ** menas keyword arguments kwarg become dictonary
   #print(type(kwargs))
    print("Record informations")
    for k,v in kwargs.items():
        print(k,"........",v)
                
display(name="rama",marks=100,age=48,GF="Sunny")
display(name="ravi",brand1="KF",brand2="RC",brand3="xyz")

# O/p:-
Record informations
name ........ rama
marks ........ 100
age ........ 48
GF ........ Sunny
Record informations
name ........ ravi
brand1 ........ KF
brand2 ........ RC
brand3 ........ xyz

# Example:-
def f1(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
    
f1(3,2,arg4=200)
f1(arg4=2,arg1=3,arg2=4)

#o/p:-
3 2 4 200
3 4 4 2

# Recursive Functions:-
#---------------------------------------------------------------------------------
# A function that calls itself recursive functions

# Example:-
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

print(factorial(4))

# O/p:- 24

# Anonymous Functions:-
#------------------------------------------------------------------------------------
# Without name---> nameless functions are called Anonymous Functions
# instance use(only one time usage)

s=lambda n:n*n
print(s(4))

#Example:1
s=lambda x:x*x
print(s(2))
print(s(3))
print(s(4))

#Example:2
s=lambda x,y:x+y
print(s(10,20))

#Example:3
s=lambda a,b: a if a>b else b
print("the biggest of {} and {} is :{}".format(10,20,s(10,20)))

#o/p:- 
the biggest of 10 and 20 is :20

# 1. filter():
#-------------------------------------------------------
# syntax: filter(function,swquence)
# filter(function,list)
# 
# Example:-
def iseven(x):
    if x%2==0:
        return True
    else:
        return False
    
l=[0,5,10,15,20,25,30]
l1=list(filter(iseven,l))
print(l1)

#o/p:- 
[0, 10, 20, 30]

# Example2:- With lambda
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1)

#o/p:- 
[0, 10, 20, 30]

#Example:3 For getting odd numbers
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2!=0,l))
print(l1)

#o/p:-
[5, 15, 25]

# 2. map():
#--------------------------------------------------------------------------------
# syntax:- map(function,sequence)
# map will return same no of elements as given in input but filter() is for filtering the values of a list or nay collections ,it return true and false
# Example:

l=[0,5,10,15,20,25,30]
l1=list(map(lambda x:x*x,l))
print(l1)

#o/p:-
[0, 25, 100, 225, 400, 625, 900]

#Example:-
l1=[1,2,3,4]
l2=[10,20,30,40]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)

#o/p:-
[10, 40, 90, 160]

# Nested Functions:-(function declared in another functions)
#-----------------------------------------------------------------------------------
# Example:-
def f1():
    def inner(a,b):
        print("the sum is",a+b)
        print("the average is",(a+b)/2)
    inner(10,20)
    inner(20,30)
    inner(100,200)
    
f1()

# Example: A function can return another function

def outer():
    print("outer function started")
    def inner():
        print("inner function executions")
    print("outer function returing inner function")
    return inner; # it means return inner function directly 

f1=outer()  # f1 is pointing to inner function
f1()

# NOTE:---
# f1=outer() # function call and return values is assign to f1
# f1=outer # for outer function we are giving another name.


# Function Decorators:-
#--------------------------------------------------------------------------------------------
# Input function====>Decorator Function====>Output function with extended functionality.
# Decorator help to make our code shorter and more pythonic.
#





