# Until and unless we are not declaring any instance variables ,don't go for instance method because calling an instace method is bit costly(as we need to access it by creating object reference).
# But in cse of class method we can access direclty with class name.

# Declartion of class Method
#----------------------------------------------------------------------------
@classmethod
def m1(cls):
    print(cls.collegename)
    print(cls.bankname)
    
#Difference between instance and class method
#---------------------------------------------------------------------------------
# 1.Inside method body if we are using atleast one instance variable then we complusory we should declare that method as instance method.
# 1.Inside method body if we are using static variables then it is highly recommended to declare that method as class method.

# 2.To declare instance method we are not required to use decorator.
# To declare class method complusory we should use @classmethod decorator.

# 3. The first argument of the instance method should be self,which is reference to current object and by using self ,we can access instance variables inside  method.
# The first argument to the class method should be cls ,which is reference variable current class object and by using that we can access static varaibles.

# 4.Inside instance method we can access both instance and static variables.
# Inside classmethod we can access only static variables and we can't access instance variables.

# 5.We can call instancer method by using object reference.
# We can access classmethod either by using object reference or by using class name, but recommended to use classname.


# Example 1
class Animal:
    legs=4  # static variable
    
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))
        
Animal.walk('Dog')

# Example 2:-
# To track number of objects created for a class
class Test:
    count=0 # static variable
    def __init__(self):
        Test.count=Test.count+1
        
    @classmethod    
    def getNoOfObject(cls):
        print('the no od object created',cls.count)
        
t1=Test()
t2=Test()
t3=Test()
t4=Test()
Test.getNoOfObject()

#-------------------------------------------static method--------------------------------------------------------------------------
# Just general utility method
# Synatx:-
@staticmethod
def sum(x,y);
  print('the sum:',x+y)
 
 Test.sum(10,20)

#Example:-

class CalMath:
    
    @staticmethod
    def add(x,y):
        print('the sum is:-',x+y)
        
    @staticmethod
    def product(x,y):
        print('product is',x*y)
        
    @staticmethod
    def avg(x,y):
        print('the avg is',(x+y)/2)
        
CalMath.add(20,30)
CalMath.product(20,30)
CalMath.avg(20,30)

# instance method vs class method vs static method;
#-----------------------------------------------------------------------------
# 1. If we are using any instance variable inside method body then we should go for instance method.We should call by using object reference only.

# 2. if we are using only static variables inside method body then this method no way related to a particular object , we should declare such type of methods as classmethos.
# We can call either by using object reference or by using class name.

# 3. If we are not using any instance varaiable and any static varaiables inside method body,to define such type of general utility methods we should go for static methods.
# We can call either by using object reference or by using class name.

# If we are not using any decorator:
#-------------------------------------------------------------------------------
# For classmethod ,@classmethod decorator is mandatory.
# For staticmethod,@staticmethod decorator is optional.

# Without any decorator the method can be either instance method or static method,If we are calling by using object reference it should be instance method.
#If we are calling by using class name then it should be static method.

# Example:-1
class Test:
    def m1():
        print('hellooo')
        
t=Test()
t.m1()

# The above code ,Python will consider the method as instance method,but we are not declaring self variable.Hence we are getting below error.
---------------------------------Error------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-2d0d5d2ddf2d> in <module>
      4 
      5 t=Test()
----> 6 t.m1()

TypeError: m1() takes 0 positional arguments but 1 was given
--------------------------------------------------------------------------------


# Example:-2

class Test:
    def m1():
        print('hellooo')
        
Test.m1()
# o/p:- hellooo

# The above code is valid and python will consider this method as static method.

# Example:- 3

class Test:
    @staticmethod
    def m1():
        print('hellooo')
        
t=Test()
t.m1()

# o/p:- hellooo

# In the above code @staticmethod decorator is given due to which it's static method,and we can call static method either by class name or class reference.


# Example:- 4

class Test:
   
    def m1(x):
        print('hellooo',x)
        
t=Test()
t.m1(10)

# In the above code ,Python will considered the m1() method as instance method bcz we are calling it by object reference and providing 
# x as self to the method,But we are passing x as argument to the method so it's consider it 2 arguments(one is self and another one is x)

------------------------------Error below---------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-a9c559cef3dc> in <module>
      5 
      6 t=Test()
----> 7 t.m1(10)

TypeError: m1() takes 1 positional argument but 2 were given
------------------------------------------------------------------------------






