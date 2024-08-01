from math import prod
import threading
def iscolorful(n):
    largest = [0]
    if 0<= n < 10:
        return True
    dig = [int(c) for c in str(n)]
    if 1 in dig or 0 in dig or len(dig) > len(set(dig)):
        return False
    products = list(set(dig))
    for i in range(len(dig)):
        for j in range(i+2, len(dig)+1):
            p = prod(dig[i:j])
            if p in products:
                return False
            products.append(p)
    largest[0] = max(n, largest[0])
    return True

def managing_ranges(start,end):
    #I should get the thread to count up the numbers in this
    #range and then have it return the count?
for i in range(10):
    start = 100000*(i-1)
    end = 100000*i


