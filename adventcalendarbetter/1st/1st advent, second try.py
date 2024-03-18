
with open("1st.txt") as file:
    content = file.readlines()
#This function takes a string, finds the numbers and adds them up
#after doing so it returns the first and the last number as an integer
numbers = ["1","2","3","4","5","6","7","8","9","0"]
print(content)
def removeLetters(b):
    x=""
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    for g in b:
        if g in numbers:
            x = x+g
    if x == "" or None:
        return()
    y = x[0]+x[-1]

    return(int(y))
#I define b as 0 so b can be added values gained from each line in content
b = 0
for i in content:
    b = b+removeLetters(i)
print(b)
letter_numbers = ["one","two","three","four","five","six","seven","eight","nine","zero"]
#print(content)
example = "threerznlrhtkjp23mtflmbrzq395three"
# I have to find number words in the string and the numbers in the string and add them to a list


def WordsToNumbers(string):
    d = 0
    letter_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
    happyList = []
    while (d+2) <len(string):
        num = string[d]+string[d+1]+string[d+2]

        if num in letter_numbers:
            happyList.append(num)
        elif len(string)-d-1 > 2:
            num = num + string[d+3]

            if num in letter_numbers:
                happyList.append(num)
            elif len(string)-d-1 > 3:
                num = num +string[d+4]

                if num in letter_numbers:
                    happyList.append(num)
        if num not in letter_numbers:
            happyList.append(string[d])
        d = d + 1
    happyList.append(string[d])
    happyList.append(string[d+1])
    return(happyList)
print(WordsToNumbers(example))

def convertLetNum(g):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    temp = []
    for x in g:

        if x.lower() == "one":  x = "1"
        elif x.lower() == "two": x = "2"
        elif x.lower() == "three": x="3"
        elif x.lower() == "four": x="4"
        elif x.lower() == "five": x="5"
        elif x.lower() == "six": x="6"
        elif x.lower() == "seven": x="7"
        elif x.lower() == "eight": x="8"
        elif x.lower() == "nine": x="9"
        elif x.lower() == "zero": x="0"
        temp.append(x)
    goodList = []
    for i in temp:
        if i in numbers:
            goodList.append(i)
    if len(goodList) ==0:
        return 0
    o = goodList[0]+ goodList[-1]
    return int(o)

H = 0
for i in content:
    print(convertLetNum(WordsToNumbers(i)))
    H = H + convertLetNum(WordsToNumbers(i))
print(H)
print(WordsToNumbers(example))




