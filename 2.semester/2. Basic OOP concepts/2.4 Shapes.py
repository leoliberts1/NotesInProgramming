import math


class Shape:
    def __init__(self,sides,):
        self.sides = sides
    def perimeter(self):
        perimeter = 0
        for side in self.sides:
            perimeter += side
        return print("The perimeter is",perimeter)
class Square(Shape):
    def __init__(self,sides):
        Shape.__init__(self,sides)
    def Area(self):
        Area = self.sides[0]**2
        return print("The Area is",Area)
class Triangle(Shape):
    def __init__(self,sides):
        Shape.__init__(self,sides)
    def Area(self):
        import math
        semiper = self.perimeter()/2
        Area = math.sqrt(semiper*(semiper-self.sides[0])*(semiper-self.sides[1])*(semiper-self.sides[2]))
        return print("The Area is",Area)
class Circle(Shape):
    def __init__(self,sides):
        Shape.__init__(self,sides)
    def Area(self):
        R = self.sides[0]/(2*math.pi)
        Area = math.pi*(R**2)
        return print("The Area is ",Area)
C1 = Circle([3])
C1.Area()
C1.perimeter()
