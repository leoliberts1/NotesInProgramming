import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""
# write code to print the value of key2

jsondata = json.loads(sampleJson)
print(jsondata["key2"])


