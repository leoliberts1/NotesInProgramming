
class NumberIsNotOddException(Exception):
    pass

def abc():
    i = int(input("enter an odd number"))
    if i%2 == 0 :
        raise NumberIsNotOddException
try:
    abc()
except:
    print("Number was even")