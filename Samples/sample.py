##################### Pickling and Unpickling(Same as serialization and deserialization in java) of Objects-------------------------


class Employee:
	def __init__(self,eno,ename,esal,eaddr):      #Contructor in python
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr
	def display(self):
		print(self.eno,'\t',self.ename,'\t',self.esal,'\t',self.eaddr)
		
e1=Employee(100,'Sunny',1000,'XYZ') # creating Employee object
e1.display()	
e2=Employee(200,'Bunny',2000,'HYD')
e2.display()


#--------Pickling of Employee Object-------------------------------#

import pickle          #pickle module
class Employee:
	def __init__(self,eno,ename,esal,eaddr):      #Contructor in python
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr
	def display(self):
		print(self.eno,'\t',self.ename,'\t',self.esal,'\t',self.eaddr)
		
with open('emp.dat','wb') as f : # wb for writting binary data
	e=Employee(100,'Sunny',1000,'Mumbai')
	pickle.dump(e,f)
	print('Pickling of Employee Object Completed')

#----------Unpickling-----------------------------------------------#
with open('emp.dat','rb') as f:  # rb to read binary data
		obj=pickle.load(f)
		print('Printing Employee Information after Unpickling')
		obj.display()  # no need for self here
	


#-----------------

import pickle,emp
f=open('emp.dat','wb')
n=int(input('Enter number of Employee:'))
for i in range(n):
	eno=int(input('Enter Employee Number:'))
	ename=input('Enter Employee Name:')
	esal=float(input('Enter Employee Salary:'))
	eaddr=input('Enter Employee Address:')
	e=emp.Employee(eno,ename,esal,eaddr)
	pickle.dump(e,f)
	
print('Employee objects pickled succesfully')	

#----------------------------emp.py----------------------------
class Employee:
	def __init__(self,eno,ename,esal,eaddr):      #Contructor in python
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr
	def display(self):
		print(self.eno,'\t',self.ename,'\t',self.esal,'\t',self.eaddr)
    
   #----------------------Unpick.py------------------------
   
   import pickle,emp
f=open('emp1.dat','rb')
print('Employee Details:-')
while True:
	try:
		obj=pickle.load(f)
		obj.display()
	except EOFError:
		print('All Employees completed')
		break
f.close()		

#---------------------------Pickling.py--------------------------------

import pickle,emp
f=open('emp1.dat','wb')
n=int(input('Enter number of Employee:'))
for i in range(n):
	eno=int(input('Enter Employee Number:'))
	ename=input('Enter Employee Name:')
	esal=float(input('Enter Employee Salary:'))
	eaddr=input('Enter Employee Address:')
	e=emp.Employee(eno,ename,esal,eaddr)
	pickle.dump(e,f)
	
print('Employee objects pickled succesfully')
