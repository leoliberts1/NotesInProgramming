def swapfirstchar():
    element = str(input("enter something"))
    newWord = element[-1],element[1:len(element)-1],element[0]
    newWord = "".join(newWord)
    return newWord
print(swapfirstchar())