
def listManipulation(list, command = "add", location = "beginning",value = None ):
    if command == "add":
        if location == "beginning":
            list.insert(0,value)
        elif location == "end":
             list.append(value)
    elif command == "remove":
        if location == "beginning":
            list = list[1:]
        elif location == "end":
            list = list[:-1]
    return print(list)

listManipulation([1,2,3,4],"remove","beginning",6)



