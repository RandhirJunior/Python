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





