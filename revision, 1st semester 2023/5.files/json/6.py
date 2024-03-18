import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class ecoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# Convert it into JSON format

fvehicle = json.dumps(vehicle.__dict__,indent=2)
#or
f2vehicle = json.dumps(vehicle,indent=2,cls=ecoder)
print(fvehicle,f2vehicle)
