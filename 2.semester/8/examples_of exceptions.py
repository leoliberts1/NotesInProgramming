

def silly():
    a = input ()
    print(1/int(a))

try:
    silly()
except ZeroDivisionError:
    print("Zero division error caugght")
except ValueError:
    print("ValueError caught")
else:
    print("Everything is fine")
finally:
    print("the end of the code")
    



