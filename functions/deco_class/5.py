#!/usr/bin/python

class student:
    """A class representing a student """
    __school_name = "xyz"  ## private member
    def __init__(self,n,a):
        self.full_name = n
        self.age = a
    def get_age(self):
        return self.age

class Cs_student(student):
    """A class extending student."""
    def __init__(self,n,a,s):
        student.__init__(self,n,a) #Call __init__ for student
        self.section_num = s
    def get_age(self):                 #Redefines get_age method entirely
        print "Age: " + str(self.age)


obj = Cs_student('john', 24, 2)
student.__school_name
