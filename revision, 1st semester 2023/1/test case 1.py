def permutatedX(Smalln, Bign):
    for i in range(Smalln,Bign+1):
        i2,i3,i4,i5 = 0 +i*2,i*3,i*4,i*5
        i,i2,i3,i4,i5 = str(i),str(i2),str(i3),str(i4),str(i5)
        iord,i2ord,i3ord,i4ord,i5ord= [],[],[],[],[]

        for element in i :
            iord.append(int(element))
        iord = sorted(iord)
        for arg in i2:
            i2ord.append(int(arg))
        i2ord = sorted(i2ord)
        if iord != i2ord :
            continue
        for arg in i3:
            i3ord.append(int(arg))
        i3ord = sorted(i3ord)
        if i3ord != iord:
            continue
        for arg in i4:
            i4ord.append(int(arg))
        i4ord = sorted(i4ord)
        if i4ord != iord:
            continue
        for arg in i5:
            i5ord.append(int(arg))
        i5ord = sorted(i5ord)
        if i5ord != iord:
            continue
        return i
        #iord = sorted(iord)
        #i2ord,i3ord,i4ord,i5ord = sorted(i2ord),sorted(i3ord),sorted(i4ord),sorted(i5ord)
        #if iord == i2ord == i3ord == i4ord == i5ord:return int(i)
        #else: continue

print(permutatedX(1,1000000))#142857
print(permutatedX(142858,10000000))#1428570
print(permutatedX(1428571,100000000))#1429857
print(permutatedX(1429858,100000000))#14285700
print(permutatedX(14285701,100000000))#14298570
#pirmais run 1min 6 s
#otrais meginajums pec optimizacijas 31 s