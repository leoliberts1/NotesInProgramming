import itertools
numbers = [1,2,3,4,5,6,7,8,9,0]
itered = itertools.permutations(numbers,)# you have to enter what you want to be permutated
#and then specify how mauy elements have to be permutated there, when nothing is specified it takes all
#of the elements always and doesnt create stuff like 12 and then 21 and then 123, just goes
#straight to 12346.... and then 21346...
summ = 0
for arg in itered:
    print(arg)
    if arg[0] != 0:
        num = ""
        for arg2 in arg:
            num+= str(arg2)
        num = int(num)
        summ+=num
print(summ)