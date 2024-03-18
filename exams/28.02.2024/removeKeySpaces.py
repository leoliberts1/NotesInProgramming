

my_dict = {'a b c': [2, 3, 5],
'b d e': [1, 8, 4],
'c f g': [9, 0, 1],
'bd e': [100, 10, 1]}
def removeKeySpaces(Element):
    import re
    newDict = {}
    for key in Element:
        letters = re.findall(r"\w",key)
        #print(letters)
        NewKey = ""
        for index in letters:
            NewKey+=index
        newDict.update({NewKey:Element.get(key)})
    #print(newDict)
    return newDict
#my_dict = {'abc': [2, 3, 5],
#'bde': [1, 8, 4],
#'cfg': [9, 0, 1]}
#should be one of these
#my_dict = {'abc': [2, 3, 5],
#'bde': [100, 10, 1],
#'cfg': [9, 0, 1]}
print(removeKeySpaces(my_dict))