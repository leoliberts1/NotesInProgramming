#To navigate I have to make a variable that shows where I am looking, It shall only have 4 states and
#if the value goues out of these parameters, it gets set to the heighest or the lowest value respectively
#showing the direction still
#I start with the value 1 - North(2 - East,3 - South, 4 - west, change it by 1), when
# It is Right or Left, when It reaches 0 or 5 it gets to reset to 4 or 1 respectivelly.
import re
import math
with open("1st") as f:
    content = f.readlines()
#print(content)
current = 1
N_val = 0
E_val = 0
S_val = 0
W_val = 0
for element in content:
    commands = re.findall("\w\d+",element)
print(commands)
for command in commands:
    if command[0] == "R":
        current +=1
    elif command[0] == "L":
        current = current-1
    if current<1:
        current = 4
    elif current >4:
        current = 1
    number = re.findall("\d+",command)
    number = int(number[0])
    #print(number)
    if current == 1:
        N_val+=number
    elif current == 2:
        E_val+=number
    elif current == 3:
        S_val+=number
    elif current == 4:
        W_val+=number
print(N_val-S_val,E_val+W_val)
print(f'N - {N_val}, W - {W_val}, E - {E_val}, S - {S_val}')
print(math.sqrt((N_val-S_val)**2)+math.sqrt((E_val-W_val)**2))
