def rev(a):
    for i in range(1,len(a)):
        x = a[i]
        for j in range(i,0,-1):
            a[j] = a[j-1]
        a[0] = x
    return(a)
mylist = [34,6,21,17]
print(mylist)
print(rev(mylist))

#rev1 = rev(mylist)
print(rev(mylist))
#a) The pourpose of the function is to reverse the list
#rev2 = rev(rev1)
print(rev(mylist))
'''
b)
[34, 6, 21, 17]
[17, 21, 6, 34]
[34, 6, 21, 17]
[17, 21, 6, 34]
'''
#rev3 = rev(rev2)
#print(rev3)

#L = [1,2,3,4,5,6]
#print(L)

#L1 = rev(L)
#print(L1)

#L2 = rev(L1)
#print(L2)

#L3 = rev(L2)
#print(L3)
#print(rev(rev(mylist)))
#print(rev(rev(rev(mylist))))