import json
data = '''[
   {
      "id":1,
      "name":"name1",
      "color":[
         "red",
         "green"
      ]
   },
   {
      "id":2,
      "name":"name2",
      "color":[
         "pink",
         "yellow"
      ]
   }
]'''

data = json.loads(data)
names = []
for person in data:
   names.append(person["name"])
print(names)