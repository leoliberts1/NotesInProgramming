


class Dog:
    def __init__(self,nameX,colorX):
        #print("Hello",name)
        self.name = nameX
        self.color = colorX
    def bark (self):
        print(self.name, "is barking")

lassie = Dog ("Lassie","black")
rocky = Dog("Rocky","white")
carli = Dog("Carli","red")
lassie.bark()
print(lassie.color)
print(carli.color)
lassie.name = "Junky"
print(lassie.name)
lassie.bark()
class person:
    pass

Samuel = person()
Deepak = person()
print(Samuel)