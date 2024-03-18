
example ="happy birthday to you"
classexample = "a.creenshotssf msaketw ttIw g?runkdw ptegh bromputecn pap ksoeda swoHa"


def reversingWords(Input):

    text = Input.split()
    text  = text[::-1]
    return text


def reversingletters(Input):
    transformed = []

    for i in Input:
        var = i[-1]+i[1:len(i)-1]+i[-0]
        #print(var)
        transformed.append(var)

    return transformed

def addRandom(Input):
    import string
    import random
    trans = []
    for i in Input:
        var = random.choice(string.ascii_letters)+i+random.choice(string.ascii_letters)
        trans.append(var)
    return trans

print(addRandom(reversingWords(example)))
def removerand(arg):
    arg2 = []
    for i in arg:
        arg2.append(i[1:len(i)-1])
    return arg2
def reverslett(arg):
    arg2 = []
    for i in arg:
        if len(i)>1:
            var = i[-1]+i[1:len(i)-1]+i[0]
            arg2.append(var)
        else :arg2.append(i)
    return(arg2)
def reversorder(text):
    text = text[::-1]
    return text
x = reversorder(reverslett(removerand(classexample.split())))
print(type(x))
y = [] +list(x)
m = classexample.split()
print(m)
print(type(m))
m = removerand(m)
print(m)
m = reverslett(m)
print(m)
m = reversorder(m)
print(" ".join(m))
#
# print(x)
# print(type(y))
# print(classexample.split())
# print(" ".join(['How', 'does', 'a', 'computer', 'get', 'drunk?', 'It', 'takes', 'screenshots.']))
# result = " ".join(y)
# print(type(result))
# print(result)
# print('[', "'", 'H', 'o', 'w', "'", ',', ' ', "'", 'd', 'o', 'e', 's', "'", ',', ' ', "'", 'a', "'", ',', ' ', "'", 'c', 'o', 'm', 'p', 'u', 't', 'e', 'r', "'", ',', ' ', "'", 'g', 'e', 't', "'", ',', ' ', "'", 'd', 'r', 'u', 'n', 'k', '?', "'", ',', ' ', "'", 'I', 't', "'", ',', ' ', "'", 't', 'a', 'k', 'e', 's', "'", ',', ' ', "'", 's', 'c', 'r', 'e', 'e', 'n', 's', 'h', 'o', 't', 's', '.', "'", ']')


