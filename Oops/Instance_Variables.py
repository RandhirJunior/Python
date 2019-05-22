#------Instance variables-----------------------------
#If the value of a variable is varied from object to object such types of variable is called instance variables.
# For every object a seperate copy of instance variable is created.

# Where we have to declare instance variables............
# 1. Inside Constructor by using self
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        
s1=Student('randhir',100)
s2=Student('ravi',300)
s3=Student('rama',600)

# 2. Inside Instance method  by using self
# Inside a method when we declare a variable by using self it's also know as instance variables.

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def info(self):
        self.marks=60
        x=10          # x is here not instance variiable ,its local varaibles.
        
s1=Student('randhir',100)
s1.info()
print(s1.__dict__)
# output is  {'name': 'randhir', 'roll': 100, 'marks': 60}

# 3. From outside of the class by using object reference

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def info(self):
        self.marks=60
        
s1=Student('randhir',100)
s1.info()
s1.age=28           # declaration of instance variable age by suing object refence s1.
print(s1.__dict__)

s2=Student('Pavan',102)
s2.wife='Renu'
print(s2.__dict__)

#output is {'name': 'randhir', 'roll': 100, 'marks': 60, 'age' :28}
# {'name': 'Pavan', 'roll': 102, 'wife': 'Renu'}

# Some more examples

class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        
    def m1(self):
        self.d=40
    
    def m2(self):
        self.e=50
        
t1=Test()
t1.m1()
print(t1.__dict__)
t2=Test()
t2.m1()
t2.s=200
t2.y=300
print(t2.__dict__)
       
# Output
#{'a': 10, 'b': 20, 'c': 30, 'd': 40}
#{'a': 10, 'b': 20, 'c': 30, 'd': 40, 's': 200, 'y': 300}

#-------How to access instance variables------------------
# within the class by using self
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
    def display(self):
        print('Hello mt name is:',self.name)
        print('My Rollno is ',self.rollno)
        
s=Student('Randhir',101)
s.display()

#Output------
#Hello mt name is: Randhir
#My Rollno is  101

# from ourside of the class by using object reference

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
    def display(self):
        print('Hello mt name is:',self.name)
        print('My Rollno is ',self.rollno)
        
s=Student('Randhir',101)

print(s.name,s.rollno)  # By using object reference

# How to delete instance variables:
#---------------------------------------------------------------------------------------
#1. Within the class :- del self.variablename
   
 class Test:
    def __init__(self):
        self.a=10
        self.b=10
        self.c=10
    def  delete(self):
        del self.b
        del self.c
t1=Test()
t1.delete()
print(t1.__dict__)

# 2. Outside of the class :- del objectrefence.variable
 
class Test:
    def __init__(self):
        self.a=10
        self.b=10
        self.c=10
    def  delete(self):
        del self.b
        del self.c
t1=Test()
t1.delete()
del t1.a
print(t1.__dict__)

#o/p :- {}

# NOTE:- Instance variables deleted from one object may not deleted from other object.Every object created it's own instance variables.

class Test:
    def __init__(self):
        self.a=10
        self.b=10
        self.c=10

t1=Test()
t2=Test()
del t1.a
del t2.b
print(t1.__dict__)
print(t2.__dict__)

# O/p:- {'b': 10, 'c': 10}
#       {'a': 10, 'c': 10}

# Examples 2:-
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    
t1=Test()
t2=Test()
t1.a=888
t1.b=999
print(t1.a,t1.b)
print(t2.a,t2.b)

#O/p:- 888 999
#      10  20


