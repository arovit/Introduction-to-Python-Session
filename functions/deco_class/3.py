#!/usr/bin/python

class student:
    """A class representing a student """
    school_name = "xyz"
    def __init__(self,n,a):
        self.full_name = n
        self.age = a
    def get_age(self):
        return self.age


obj = student('john', 24)
print obj.full_name
print student.school_name


# --
