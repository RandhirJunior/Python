# If the value not varied from object to object ,such types of variable we have to declare at class level and such type of variable is called static variable.
# static variable:- For all objects a single copy maintained at class level.

class Student:
    cname='IIT'
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
s1=Student('Ram',101)
s2=Student('Sayam',102)

print(s1.name,s1.rollno,Student.cname)
print(s2.name,s2.rollno,Student.cname)

# O/P :- Ram 101 IIT
#        Sayam 102 IIT
