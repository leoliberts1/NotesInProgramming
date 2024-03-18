class Student:
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        New_Student = Student(self.name+"+"+other.name)
        return New_Student
    def __str__(self):
        return self.name

s1 = Student("Sandy")  # name
s2 = Student("Spili")  # name
s3 = Student("Waile")  # name
print(s1 + s2 + s3)# should print Sandy+Spili+Waile