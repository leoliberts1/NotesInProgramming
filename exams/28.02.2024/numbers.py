#The first row's largest and smallest values are 9 and 1, and their difference is 8.
#The second row's largest and smallest values are 7 and 3, and their difference is 4.
#The third row's difference between the largest value (8) and the smallest value (2) is 6.
#In this example, the hidden number would be 8 + 4 + 6 = 18.
#What is the secret number in the data file attached to this question?
def sNumbers(fileName):
    import re
    import math
    with open(fileName,"r") as f:
        data = f.readlines()
    #print(data)
    lineNum = []
    for element in data:
        if data.index(element) != len(data)-1:
            lineNum.append(element[:-1])
        else: lineNum.append(element)
    num = []
    for index in data:
        allnumbers = re.findall("\d+",index)
        num.append(allnumbers)
    #print(num)
    #print(lineNum)
    justNumbersList = []
    for arg in num:
        SmallJustNumbers = []
        for arg2 in arg:
            SmallJustNumbers.append(int(arg2))
        justNumbersList.append(SmallJustNumbers)
    #print(justNumbersList)
    MaxMinNUmbers = []
    for arg in justNumbersList:
        maxminSmall = []
        maxminSmall.append(max(arg))
        maxminSmall.append(min(arg))
        MaxMinNUmbers.append(maxminSmall)
    #print(MaxMinNUmbers)
    differences = []
    for arg in MaxMinNUmbers:
        differences.append(math.sqrt((arg[0]-arg[1])**2))
    #print(differences)
    secret_num = 0
    for arg in differences:
        secret_num+= arg
    #print(secret_num)
    return print(int(secret_num))

sNumbers("randomsmall.txt")
sNumbers("randome_ums.txt")