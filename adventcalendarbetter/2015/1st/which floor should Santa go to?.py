with open ("map") as f1:
    Map = f1.read()
print(Map)
floor = 0
index = 0
for element in Map:
    if element == "(":
        floor +=1
    else :
        floor = floor-1
    index+=1
    if floor == -1:
        print(index)
print(floor)