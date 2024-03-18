mystring = "some blushit"

x = mystring.ljust(178,"d")
print(x)
for arg in range(1,10):
    for arg2 in range(1,10):
        print(f'{arg} x {arg2} = {arg*arg2}' ,end=";")
    print("")