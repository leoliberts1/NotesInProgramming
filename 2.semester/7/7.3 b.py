
def frange(start,end,step):
    while start< end:
        yield start
        start+= step


for c in frange(0.3,10.2,3.2):
    print (c)