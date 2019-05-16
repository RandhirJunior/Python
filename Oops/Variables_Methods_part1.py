'''
#Inside Python class
# 3 types of variables are there
#1. Instance variables /Object level variables
--------------------------------------------------------------
   1.     
#2. Static variables / class level variables
---------------------------------------------------------------

#3. Local variables /Method variable
---------------------------------------------------------------
# 3 types of methods are there .......

1. instance methods /Object related methods
---------------------------------------------------------------

2. class methods /Utility methods
      3. static methods	
'''
		 
class Student:
    clgname='Indian Institue of Technology'                  # declration of static variable
    def __init__(self,x,y):                                  # here x and y are local varaibles            
        self.name=x                                          # instance varaibles declration i.e self.name
        self.rollno=y

    def display(self):
        print('methos execution..')
        print('Hello Myself is:',self.name)
        print('My Rollno is',self.rollno)

    @classmethod	#decrator 
    def getCollegeName(cls):
        print('College Name is',cls.clgname)
		

	@staticmethod
	def findAverage(x,y):
			print('Average is',(x+y)/2)

s1=Student('Randhir',200)
s1.findAverage(10,20)
Student.findAverage(30,40)
Student.getCollegeName()

# we can acess static methos either by object reference or by class name

















