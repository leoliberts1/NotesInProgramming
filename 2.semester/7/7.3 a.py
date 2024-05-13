def myrange(start,end,step):
    while start < end:
        yield start
        start += step


for c in myrange(0,10,3):
    print (c)

print(myrange(0,10,3))