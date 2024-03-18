import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

print("Started writing JSON data into a file")
with open("sampleJson.json","w") as f:
    f.write(json.dumps(sampleJson,sort_keys=True,indent=2))
    