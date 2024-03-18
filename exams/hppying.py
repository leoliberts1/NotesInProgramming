def squaresum(num):
    squaresum = 0
    for i in str(num):
        squaresum += int(i) ** 2
    return squaresum


def happynumbers(n):
    happylist = []
    i = 1
    while len(happylist) < n:
        sumlist = [squaresum(i)]
        while sumlist.count(1) != 1 or sumlist.count(145) != 1:
            sumlist = [squaresum(sumlist[0])]
            if sumlist[0] == 1:
                happylist.append(i)
                i = i + 1
                sumlist = [squaresum(i)]
                break
            if sumlist[0] == 145:
                i = i + 1
                sumlist = [squaresum(i)]

    return happylist


print(happynumbers(10))