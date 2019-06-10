# Method level variables are called local variables.

class Test:
    def m1(self):
        a=100
        print(a)
    def m2(self):
        a=999
        b=200
        print(b)
        
t=Test()
t.m1()
t.m2()

#Example 2:

class Test:
    def avgerage(self,list):
        result=sum(list)/len(list)
        print(result)
        
        
t=Test()
t.avgerage([10,20,30,40])

#---------------------Global Variable---------------------------------------------------------

x=100
class Test:
    def m1(self):
        print(x)
    def m2(self):
        print(x)
t=Test()
t.m1()
t.m2()

# From the class we can access global variable directly.
# Within a method of a class we can declare global varibale by using global keyword.
#---------------------------------------------------------------------------------------
#-------------------Banking Application Code--------------------------------------------

import sys
class Customer:
    '''Customer class with bank related operations'''
    bankname='SBI' # static variable
    
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
        
    def deposite(self,amount):
        self.balance=self.balance+amount
        print('After deposite the balance:',self.balance)
        
    def withdraw(self,amount):
        if amount>self.balance:
            print('Insuffient fund')
            sys.exit()
       
        self.balance=self.balance-amount
        print('After withdraw the balance is',self.balance)
        
print('Welcome to ',Customer.bankname)
name=input('Enter your Name')
c=Customer(name)
while True:
    print('d-Deposite\nw-Withdraw\ne-Exit')
    option=input('choose your options')
    if option.lower()=='d':
        amount=float(input('Enter the amount to deposite'))
        c.deposite(amount)
        
    elif option=='w' or option=='W':
        amount=float(input('Enter the amount to Withdraw'))
        c.withdraw(amount)
        
    elif option=='e' or option=='E':
        print('Thanks for Banking')
        sys.exit()
        
    else:
        print('Choose valid option')
        
#




