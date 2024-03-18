import json






data = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'
data = json.loads(data)
print(data,data["name"])
class Vehicle:
    def __init__(self,name,engine,price):
        self.name = name
        self.engine = engine
        self.price = price

vehicleobj = Vehicle(data["name"],data["engine"],data["price"])

print(vehicleobj.name, vehicleobj.engine, vehicleobj.price)
