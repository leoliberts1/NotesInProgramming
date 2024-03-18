n = 1
i = 2
sum = 0
while i < 4000000:
    t = n+i
    if t%2 == 0:
        sum+=t
    n = i
    i = t
print(sum+2)







