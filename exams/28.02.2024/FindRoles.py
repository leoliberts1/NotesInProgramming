def find_roles(mydict, val):
   Roles = []
   for Role in mydict:
       if val in mydict.get(Role):
           Roles.append(Role)
   return Roles

d = {"teacher": ["Mark", "James", "Sandy"],
     "police":  ["James", "Mary", "Danny"],
     "gardener":["Mark", "Sandy", "James"] }

print (find_roles(d, "Mark"))
# Expected Output: ["teacher", "gardener"]

print (find_roles(d, "James"))
# Expected Output: ["teacher", "police", "gardener"]