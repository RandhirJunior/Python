#Plan acts as Blue print/Template for the buildings
#Plan is nothing but class.

#The buildings constructed based on the plan ==>objects
#The pysical existence of a class is nothing but objects.

#Once class is ready===> multiple objects we can create.

class Student:
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
	def talk(self):
		print("Hello My name is",self.name)
		print("My rollno is",self.rollno)
s=Student('Randhir',100)
print(s.name)
print(s.rollno)
s.talk()		
s1=Student('Sunny',200)
s1.talk()
