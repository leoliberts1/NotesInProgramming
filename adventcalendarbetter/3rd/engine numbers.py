with open("example") as f1:
    text = f1.readlines()
print(text)
def remove_n(input):
    fixed = []
    for i in input:
        fixed.append(i.replace("\n",""))
    return fixed
text = remove_n(text)
print(text)
first = 396
numbers = {}
numbersForNow = 0
specialChar = {}
realNumbers = []
for i in text:
    for index in i:
        if index.isdigit() == True:
            if numbersForNow == 0 :
                first = i.index(index)
            numbersForNow = numbersForNow + int(index)*(10**(i.index(index)))


        if index.isdigit() != True and first!=396:
            numbers.update({f'list - {text.index(i)}, in the list - {i.index(index)}' : f'from {first}:{i.index(index)} number - {numbersForNow}'})
            first = 396
            numbersForNow = 0
        elif index != "." and index.isdigit() != True:
            specialChar.update({f'{text.index(i)} and {i.index(index)}' : index})


print( numbers)
print(specialChar)


#for (key,value) in

