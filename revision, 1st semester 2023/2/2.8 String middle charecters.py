#First check if the entered string is longer thatn 7 charecters
#If I get it // by 2 I will get the index of the middle charecter, then I can just return
#the charecters from -1 from the found element untill element +2
def middlechar():
    info = str(input("Write something"))
    if len(info) >6:
        if len(info) %2 != 0 :return("".join(info[len(info)//2-1:len(info)//2+2]))
    return("not good enough")
print(middlechar())