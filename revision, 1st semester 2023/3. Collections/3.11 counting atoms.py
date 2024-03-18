#Import regurlar expressions that magically find
import re
pieces = re.findall("[A-Z][a-z]?|[0-9]+", "C12H10ClN2O5S")
print (pieces)
pieces2 = re.findall("[A-Z][a-z]?|[0-9]+","Na3PO4")
print(pieces2)



def HowManyAtoms(pieces):
    numbers = []
    for i in range(2, 200):
        numbers.append(str(i))
    for element in pieces:
        if element not in numbers:
            if element != pieces[-1] and pieces[pieces.index(element)+1] not in numbers:
                print(f'{element} has one atom')
            elif element != pieces[-1] and pieces[pieces.index(element)+1] in numbers:
                print(f'{element} has {pieces[pieces.index(element)+1]} atoms')
            elif element == pieces[-1]:
                print(f'{element} has one atom')
HowManyAtoms(pieces)