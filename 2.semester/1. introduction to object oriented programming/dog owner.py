class dog:
    def __init__(self,name):
        self.name = name
        self.color = None
        self.owner = None
    def setOwner(self,owner):
        self.owner = owner
        owner.dog = self
d = dog("Lassie")
class person:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.dog = None
    def setDog(self,dog):
        self.dog = dog
        dog.owner = self
p = person("Mr Smith")
#Bad to assign the values from "outside" the object
#d.owner = p
p.setDog(d)


print(p.dog.name)
print(d.owner.name)