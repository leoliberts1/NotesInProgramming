class animals:
    def __init__(self,Name,Age,weight):
        self.name = Name
        self.age = Age
        self.weight = weight
    def makeNoise(self):
        print(self, "moved the bushes")
    def eat(self):
        print(self,"just ate")
    def sleep(self):
        print(self,"just slept")
    def birthyear(self):
        print(f'{self.name} was born in {2024-self.age}')
class person:
    def __init__(self,name):
        self.name = name
    def feed(self,animal,food):
        print(f'{self.name} just fed {animal.name} : {food}')
Animals = [
    animals("Tiger32",12,121),
    animals("Lion42",4,131),
    animals("Zebra12",12,11),
    animals("Bison23",4,121),
    animals("Turtle Harriet",194,200)
]
caretaker = person("Joe")
for animal in Animals:
    caretaker.feed(animal,"Apple")
for animal in Animals:
    animal.birthyear()