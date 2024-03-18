class CarInsuranceCompany():
    def __init__(self, name):
        self.name = name
        self.agents = []
        self.costumers = []
    def getAgent(self,agent):
        self.agents.append(agent.name)
        agent.employer = self.name
class Agent():
    def __init__(self,name,id):
        self.name = name
        self.costumers = []
        self.employer = None
        self.address = None
        self.id = id
    def addCostumer(self,Costumer):
        self.costumers.append(Costumer.name)
        Costumer.agent = self.name
class costumer():
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.address = None
        self.cars = []
        self.agent = None
        self.CarInsurance = None
    def __str__(self):
        return self.name
    def addCar(self,car):
        self.cars.append(car)
        car.Owner = self.name
class Car():
    def __init__(self,model,Year,Numberplate):
        self.model = model
        self.Year =Year
        self.Numberplate = Numberplate
        self.Owner = None
    def __str__(self):
        return self.Numberplate + " and the owner is "+self.Owner

car1 = Car("Model T",1935,"W316F",)
agent1 = Agent("Samuel Jackson",1234)
p1 = costumer("Dwane the ROCK Johnson",12123)
c1 = CarInsuranceCompany("Freedom")
p1.addCar(car1)
agent1.addCostumer(p1)
c1.getAgent(agent1)

print(car1)
print(agent1.costumers)
print(p1)
print(c1.agents)