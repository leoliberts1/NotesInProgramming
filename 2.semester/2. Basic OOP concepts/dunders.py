class person():
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
class University:
    def __init__(self):
        self.students = []
    def enroll(self,student):
        self.students.append(student)
    def __len__(self):
        return len(self.students)
class length:
    def __init__(self,dimension,unit):
        self.dimension = dimension
        self.unit  = unit
    def __add__(self, other):
        if self.unit == "m":
            self.unit = "cm"
            self.dimension = self.dimension*100
        if other.unit == "m":
            other.unit = "cm"
            other.dimension = other.dimension*100
        result = (self.dimension+other.dimension,"cm")
        return length(result[0],result[1])
    def __str__(self):
        return str(self.dimension)+ " " + self.unit
x1 = length(100,"m")
x2 = length(200,"cm")

print(x1+x2)

p1 = person("Sam",23)
p2 = person("Sam",23)
imc = University()
imc.enroll(p1)
imc.enroll(p2)

print(id(p1))
print(id(p2))

print(p1 == p2) #p1.__eq__(p2)
print(len(imc))
