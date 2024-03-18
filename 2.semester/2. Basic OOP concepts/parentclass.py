class Person():
    def __init__(self,name,dob,address,age):
        self.name = name
        self.dob = dob
        self.address = address
        self.age = age
    def speak(self):
        print(f'Hello, my name is {self.name}')

class Teacher(Person):
    def __init__(self,salary,name,dob,address,age):
        Person.__init__(self,name,dob,address,age)
        self.salary = salary
    def speak(self):
        print(f'Hello my name is {self.name} and I earn {self.salary}')
class student(Person):
    def __init__(self,name,age,dob,address,studyProg):
        Person.__init__(self,name,dob,address,age)
        self.studyprog = studyProg
        self.fees = None
    def speak(self):
        print(f'Hello, my name is {self.name} and I am studying {self.studyprog}')

class NonEUStudent(student):
    def __init__(self,name,age,dob,address,studyprog):
        super().__init__(name,age,dob,address,studyprog)
        self.fees = 10000
class EUStudent(student):
    def __init__(self,name,age,dob,address,studyprog):
        super().__init__(name,age,dob,address,studyprog)
        self.fees = 400

P1 = NonEUStudent("Black Beard",28,1622,"Haiti","Business")
s1 = EUStudent("Jack Sparrow",27,1647,"Carribean","INF")
print(s1.name)
t1 = Teacher(200000,"Peter Parker",2001,"New York",23)
print(t1.salary)
t1.speak()
s1.speak()
justPerson = Person("Samuel",1987,"Marss",56)
justPerson.speak()
P1.speak()