def permutatedx(start,stop):
    for number in range(start,stop+1):
        def sorted_list(number):
            sorted_one = []
            for arg in list(str(number)):
                sorted_one.append(int(arg))
            return sorted(sorted_one)
        list_to_compare = list(str(number))#transforms it into a list, splits everything apart, just by being made
        list_actual = []
        for arg in list_to_compare:
            list_actual.append(int(arg))
        list_actual = sorted(list_actual)
        number2,number3,number4,number5 = number*2,number*3,number*4,number*5
        if list_actual == sorted_list(number2) and list_actual == sorted_list(number3) and list_actual == sorted_list(number4) and list_actual == sorted_list(number5):
            return number



print(permutatedx(1,1000000))#142857
print(permutatedx(142858,10000000))#1428570
print(permutatedx(1428571, 100000000))# 1429857
print(permutatedx(1429858, 100000000))#  14285700
print(permutatedx(14285701, 100000000))#  14298570