from random import randint
class Student:
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob
        self.university = None
        self.exams = []
    def takeExam(self,exam):
        self.exams.append(exam)
        exam.notes.update({self:randint(1,5)})
    def __repr__(self):
        return self.name
class University:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.exams = []
    def enroll(self,student):
        student.university = self
        self.students.append(student)
    def stats(self):
        for student in self.students:
            print(f'{student} took {len(student.exams)} exams')
            for exam in student.exams:
                print(f'          Got {exam.notes.get(student)} in {exam}')

class Exam:
    def __init__(self,name):
        self.name = name
        self.notes = {}
    def __repr__(self):
        return self.name
    def stats(self):
        avg_grade = 0
        for student in self.notes:
            avg_grade += self.notes.get(student)
        avg_grade = avg_grade/len(self.notes)
        print(f'{self} was taken by {len(self.notes)} students. average grade was  = {avg_grade}')

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