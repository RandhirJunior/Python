#Plan acts as Blue print/Template for the buildings
#Plan is nothing but class.

#The buildings constructed based on the plan ==>objects
#The pysical existence of a class is nothing but objects.

#Once class is ready===> multiple objects we can create.

'''
1.self is a reference variable which is always pointing to current object.
   Within the python class to refer current object we should use self variable.
2. The first argument to the constructor and instance method should be self.
3. PVM is responsible to provide value for self argument and we are not required to provide explicitly.   
4. By using self we can declare instance variable
5. By usingself we can access instance variable.
'''

class Student:
	def __init__(self,name,rollno):   #This is the constructor
		self.name=name
		self.rollno=rollno
	def talk(self):
		print("Hello My name is",self.name)
		print("My rollno is",self.rollno)
s=Student('Randhir',100)  #Object Creation step and s is the reference of Student object
print(s.name)
print(s.rollno)
s.talk()	# Python virtual machine(PVM) is responsible to provide self.	
s1=Student('Sunny',200)
s1.talk()
