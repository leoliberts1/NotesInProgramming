class Person:
    def __init__(self,name):
        self.name = name
        self.pet = None
class Pet:
    def __init__(self,name,house):
        self.name = name
        self.livesIn = house
    def __str__(self):
        return self.name +" that live in a "+ self.livesIn
class Dog(Pet):
    def __init__(self,name):
        house = "Kennel"
        Pet.__init__(self,name,house)
class Cat(Pet):
    def __init__(self,name):
        house = "CatHouse"
        Pet.__init__(self,name,house)
class Fish(Pet):
    def __init__(self,name):
        Pet.__init__(self,name,"Aquarium")

H = Dog("Husky")
print(H)
