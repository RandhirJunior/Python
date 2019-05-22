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

