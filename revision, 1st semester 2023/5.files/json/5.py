import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# write code to print the value of salary
data = json.loads(sampleJson)
print(data)
print(data["company"]["employee"]["payble"]["salary"])
