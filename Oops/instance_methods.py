#instance methods

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
