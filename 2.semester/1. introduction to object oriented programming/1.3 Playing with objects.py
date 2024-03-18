class Student:
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob
        self.university = None
        self.grades = {}

    def takeExam(self,exam):
        import random
        mark = random.randint(1,5)
        self.grades.update({exam:mark})
        exam.grades.append(mark)


class University:
    def __init__(self,name):
        self.name = name
        self.students = []
    def enroll(self,student):
        self.students.append(student)
        student.university = self
    def stats(self):
        for student in self.students:
            print(f'{student.name} took {len(student.grades)} exams')
            for exam in student.grades:
                print(f'got {student.grades.get(exam)} in {exam.name}')
class Exam:
    def __init__(self,name):
        self.name = name
        self.grades = []
    def stats(self):
        average = 0
        for grade in self.grades:
            average+=grade
        average = average/len(self.grades)
        print(f'{self.name} was taken by {len(self.grades)} students and the average score was {average}')





s1= Student ("Sandy", "24.01.1992") # name, dob
s2= Student ("Spili", "14.10.1993") # name, dob
s3= Student ("Waile", "04.06.1994") # name, dob

imc = University ("FH Krems")

imc.enroll(s1)
imc.enroll(s2)
imc.enroll(s3)

e1 = Exam("Programming II")
e2 = Exam("Software Eng")
e3 = Exam("Creativity")
# assign a random value as grade
#I will assign a random value from 1 to 5
s1.takeExam (e1)
s2.takeExam (e1)
s3.takeExam (e1)

s1.takeExam (e2)
s2.takeExam (e2)

s1.takeExam (e3)
s3.takeExam (e3)
# print statistics
imc.stats()

e1.stats()
e2.stats()
e3.stats()