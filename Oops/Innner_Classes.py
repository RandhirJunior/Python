# How to access member of one class inside another class:
#-----------------------------------------------------------------------------------------------------------------------------
class Employee:
    def __init__(self,eno,ename,esal): # instance method
        self.eno=eno
        self.ename=ename
        self.esal=esal
        
    def display(self): #its a instance method
        print('Employee number',self.eno)
        print('Employee name',self.ename)
        print('Employee salary',self.esal)
        
class Test:
    def modify(emp):     # its a static method
        emp.esal=emp.esal+10000
        emp.display()
        
e=Employee(12345,'Randhir',50000)
Test.modify(e)

#----------------------------Inner Class---------------------------------------------------------------------------------------
