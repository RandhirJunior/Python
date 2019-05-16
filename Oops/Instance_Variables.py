#------Instance variables-----------------------------
#If the value of a variable is varied from object to object such types of variable is called instance variables.
# For every object a seperate copy of instance variable is created.

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        
s1=Student('randhir',100)
s2=Student('ravi',300)
s3=Student('rama',600)

# Where we have to declare instance variables............
# 1. Inside Constructor by using self
