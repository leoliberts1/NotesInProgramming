class Vehicle:
    def __init__(self,numberPlate,Seating):
        self.color = "white"
        self.number = numberPlate
        self.seating_capacity = Seating
    def fare(self):
        cost = self.seating_capacity*100
        return print("The cost for this fare is",cost)
class Car(Vehicle):
    def __init__(self,numberplate):
        Vehicle.__init__(self,numberplate,5)
class Buss(Vehicle):
    def __init__(self,numberplate):
        Vehicle.__init__(self,numberplate,50)
    def fare(self):
        cost = self.seating_capacity*100*1.1
        return print("The fare will cost",int(cost))
B1 = Buss("F124GJ")
B1.fare()
C1 = Car("HDGD90")
C1.fare()