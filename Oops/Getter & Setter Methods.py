# Setter method Syntax
# def setVariablename(self,variableName):
#    self.variableName=variableName
#
#  Example:-
#  def setMarks(self,Marks):
#      self.Marks=Marks
#
#   def getMarks(self):
#       return self.Marks

# Examples 1:

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
    
  
