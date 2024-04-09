def dumplings(arg):
    if arg>1:
        print("still going")
        dumplings(arg/2)
        dumplings(arg/2)
dumplings(1)#0
#potato(2)#1
dumplings(4)#3
#potato(8)#7
#potato(16)#15
#potato(32)#31