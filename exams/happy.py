
"""
def happynumbers(n):
    happy = []
    start = 1
    start2 = 1
    number_now = 0
    while len(happy)<n:
        number_now = start*start
        if number_now == 1:
            happy.append(start2)
            start2+=1
            start = 0+start2
        save = 0
        for numbers in list(str(number_now)):
            save+=int(numbers)*int(numbers)
        if save == start2 and save !=1:
            start2+=1
            start = 0+start2
        else:start = 0+number_now
    return(happy)
print(happynumbers(5))

"""


def HappyNumber2(n):
    start = 0+n
    num = 0
    def Happyrec(arg,start):
        num = 0
        for element in str(arg):
            num+= int(element)**2
        if int(num) == 1: return f'{start} is Happy rec'
        elif int(num) == start or int(num) == 4:return f'{start} is not Happy rec'
        else:
            return Happyrec(int(num),start)
    for element in str(start):
        element = int(element)**2
        num+=element
    if int(num) == 1:
        return f'{start} is Happy'
    else: return Happyrec(int(num),start)
print(HappyNumber2(347))