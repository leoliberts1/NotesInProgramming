def reversibles (n):
    GoodNumbers = []
    start = 1
    while len(GoodNumbers) < n:
        number = start+int(str(start)[::-1])
        if (str(start)[::-1])[0] == "0":
            start+=1
            continue
        isodd = True
        for arg in list(str(number)):
            if int(arg)%2 ==0 :
                # GoodNumbers.append(start)
                # start += 1
                isodd = False
        if isodd:
            GoodNumbers.append(start)
        start+=1
    return(GoodNumbers)
#Hint: There are 120 reversible numbers below 1000.
print(reversibles(120))
print(list(str(563)))
for x in reversibles (10):
        print (x)