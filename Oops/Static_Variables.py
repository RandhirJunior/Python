# If the value not varied from object to object ,such types of variable we have to declare at class level and such type of variable is called static variable.
# static variable:- For all objects a single copy maintained at class level.

class Student:
    cname='IIT'
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
s1=Student('Ram',101)
s2=Student('Sayam',102)

print(s1.name,s1.rollno,Student.cname)
print(s2.name,s2.rollno,Student.cname)

# O/P :- Ram 101 IIT
#        Sayam 102 IIT

# What are various places are there to declare static variables?.
#------------------------------------------------------------------------------
# 1. Within the class directly but from outside of any method
# 2. Inside constructor by using classname.
# 3. Inside instance metod by using classname.
# 4. Inside classmethod by using cls variable or classname
# 5. Inside staticmethod by using classname.
# 6. From outside of class by using classname.

class Test:
    a=10
    def __init__(self):
        Test.b=20
    def m1(self):
        Test.c=30
    
    @classmethod
    def m2(cls):
        cls.d=40
        Test.e=50
        
    @staticmethod
    def m3():
        Test.f=60
t=Test() 
t.m1()
Test.m2()
Test.m3()
Test.g=70

print(Test.__dict__)  # It will print only class level static variables i.e a and g

# How to access static variables:-
#-------------------------------------------------------------------------
# We can access static variables either by classname or by object reference.
#
# Within the class
#--------------------
# classname,self,cls
#
# Outside of the class:
#-------------------------------
# object reference,classname

#Examples 1:

class Test:
    a=10
    def __init__(self):
        print('Inside constructor')
        print(Test.a)
        print(self.a)
    def m1(self):
        print('Inside instance method')
        print(Test.a)
        print(self.a)
    @classmethod
    def m2(cls):
        print('Inside class method')
        print(Test.a)
        print(cls.a)
        
    @staticmethod
    def m3():
        print('Inside sttatic method')
        print(Test.a)
        
t=Test()
t.m1()
t.m2()
t.m3()
print('From outside of the class')
print(Test.a)
print(t.a)
#------------------------------------------------------------------------------------

# How to modify static variables:-
#-------------------------------------------------------------------------------------
# 1. Within the class we should use classname,cls variables.
# 2. From outside of the class: only classname.

# Example:-
class Test:
    a=10
    def __init__(self):
        self.a=20
        
t=Test()
print(Test.a)   #  It call static variable i.e a=10
print(t.a)      # here it calls instance variable i.e a=20

# Example:-

class Test:
    a=10
    def __init__(self):
        Test.a=20
    @classmethod
    def m1(cls):
        cls.a=30
        Test.a=40
        
    @staticmethod
    def m2():
        Test.a=50
        
t=Test()
t.m1()
t.m2()
Test.a=60                 # From outside of the class
print(Test.a)   
print(t.a)

# How to delete static variable:-
#-----------------------------------------------------------
# within the class we should use classname,cls variables
# From outside of the class: only classname

# Example:- 
class Test:
    a=10
    def m1(self):
        del Test.a
        
print(Test.__dict__)
t=Test()
print(Test.__dict__)


