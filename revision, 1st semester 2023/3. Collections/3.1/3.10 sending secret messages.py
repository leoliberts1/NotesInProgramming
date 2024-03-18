message = "a.creenshotssf msaketw ttIw g?runkdw ptegh bromputecn pap ksoeda swoHa"
message = message.split(" ")
print(message)
message2 = []
for arg in message:
    message2.append(arg[1:len(arg)-1])
print(message2)
message = []
for element in message2:
    if len(element) > 2: message.append(element[-1]+element[1:len(element)-1]+element[0])
    elif len(element) == 2: message.append(element[-1]+element[0])
    else: message.append(element)
print(message)
message = message[::-1]
print(message)