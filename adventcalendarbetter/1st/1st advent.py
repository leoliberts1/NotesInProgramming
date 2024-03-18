
with open("1st.txt") as file:
    content = file.readlines()
#print(content)
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
b=0
for i in content:
    b = b+removeLetters(i)

#print(b)
letter_numbers = ["one","two","three","four","five","six","seven","eight","nine","zero"]

example = "two1nine"
happyList = []
def returning_letter_numbers(k):
    x = len(k)
    b = 0
    while x > 2 :
        num = k[b] + k[b+1] + k[b+2]
        if num in letter_numbers:
            happyList.append(num)
        if x >3:
            num = k[b] + k[b+1] + k[b+2]+k[b+3]
            #print(f'{num} 4')
            if num in letter_numbers:
                happyList.append(num)

        if x>4:
            num =k[b] + k[b+1] + k[b+2] +k[b+3]+ k[b+4]
            #print(f'{num} 5')
            if num in letter_numbers:
                happyList.append(num)
            else:
                happyList.append(k[b])
        b+=1
        x = x-1
    return((happyList))
#print(returning_letter_numbers(example))
def convertLetNum(g):
    temp = []
    for x in g:

        if x.lower() == "one":
            x = "1"
        elif x.lower() == "two":
            x = "2"
        elif x.lower() == "three":
            x="3"
        elif x.lower() == "four":
            x="4"
        elif x.lower() == "five":
            x="5"
        elif x.lower() == "six":
            x="6"
        elif x.lower() == "seven":
            x="7"
        elif x.lower() == "eight":
            x="8"
        elif x.lower() == "nine":
            x="9"
        elif x.lower() == "zero":
            x="0"
        temp.append(x)

    return(temp)
example2 = ['threerznlrhtkjp23mtflmbrzq395three\n']
#print(convertLetNum(["one","7","two","hjsdg",]))
#print(content)

#print(content)
#print()
print(returning_letter_numbers(example2))
print(removeLetters(convertLetNum(returning_letter_numbers('threerznlrhtkjp23mtflmbrzq395three\n'))))
print(removeLetters(convertLetNum(returning_letter_numbers('6mfbqtzbprqfive'))))
print(returning_letter_numbers('threerznlrhtkjp23mtflmbrzq395three\n'))

