#instance methods
#If we are using atleast one instance variable ---->instance methods.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):       # instance method ,bcz we are accessing instance variable.The first arguments of the instance method should be self
        print('Hi',self.name)
        print('Your markks are',self.marks)
        
    def grade(self):
        if self.marks>=60:
            print('First Grade')
        elif self.marks>=50:
            print('Second Grdae')
        elif self.marks>=35:
            print('You got Third Grdae')
        else:
            print('You are Fialed')

n=int(input('Enter Number of Students:'))
for i in range(n):
    name=input('Enter Name:')
    marks=int(input('Enter Marks:'))
    s=Student(name,marks)
    s.display() # Calling instance method
    s.grade()  # Calling instance method
    print('*'*20)

# setter and getter methods--------------------------------------------------
# setter method:- to set the data to the object.
# getter method:- to get the data from the object.

#setter Syntax:---
def setVariableName(self,variableName):
    self.varaibleName=variableName
    
def setMarks(self,marks):
    self.marks=marks
    
# getter Syntax:--
def getMarks(self):
    #//Validation stuff
    return self.marks
    
#---------------------------------------------------------------------------------------------
#print(s.name) // direct access no validations
#print(s.getName()) // Hiding data behind method --->Encapuslation
#
#s.name='randhir' // not good programming
#
#-----------------Examples-----------------------------------------------------------------------------
class Student:
   def setName(self,name):
    self.name=name
    
   def getName(self):
    return self.name
   
   def setMarks(self,marks):
    self.marks=marks
    
   def getMarks(self):
    return self.marks

n=int(input('Enter Number of Students:'))
for i in range(n):
    name=input('Enter Name:')
    marks=int(input('Enter Marks:'))
    s=Student()
    s.setName(name)
    s.setMarks(marks)
    
    print('Hi',s.getName())
    print('Your Marks are',s.getMarks())
    print('*'*20)
#
    
    
   
