#I have to find the first place I visit twice
#I can make a dictionnary, where I add all the
#I just have to calculate all the coordinates I visit, and add them to a list only if They are not already there
#If they are I have to break the loop and return the coordinates which I visited twice first
import re
import math

def FirstPlace(document):
    with open(document) as f:
        content = f.readlines()
    print(content)
    for element in content:
        commands = re.findall("\w\d+",element)
    print(commands)
    #North and east values that can go into negatives, since that can just as well describe where
    #the person is located
    N_value = 0
    E_value = 0
    #Orientation says where you are facing 1-North,2-East,3-South,4-West
    orientation = 1
    # Visited locations list
    vLocations = [[0,0]]
    for command in commands:
        number = re.findall("\d+",command)
        number = int(number[0])
        command = command[0]
        prevN = 0+N_value
        prevE = 0+E_value
        if command == "R":
            orientation += 1
        elif command == "L":
            orientation -= 1
        if orientation > 4:
            orientation = 1
        elif orientation <1:
            orientation = 4
        if orientation == 1:
            N_value += number
        elif orientation == 2:
            E_value += number
        elif orientation == 3:
            N_value -= number
        elif orientation == 4:
            E_value -= 1
        current_visited = []
        if N_value > prevN and E_value > prevE:
            




FirstPlace("intersection1")