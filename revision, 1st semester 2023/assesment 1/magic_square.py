




def complete_the_square (matrix):
    list1 = matrix[0]
    list2 = matrix[1]
    list3 = matrix[2]
    perfect_sum = 15
    summ1 = 0
    summ2 = 0
    summ3 = 0
    for arg in list1:
        summ1+=arg
    for arg in list2:
        summ2 +=arg
    for arg in list3:
        summ3 +=arg
    if summ1 != perfect_sum:
        return perfect_sum-summ1
    elif summ2 != perfect_sum:
        return perfect_sum-summ2
    elif summ3 != perfect_sum:
        return perfect_sum-summ3

print (complete_the_square ([[6, 0, 8], [7, 5, 3], [2, 9, 4]])) # returns 1
print (complete_the_square ([[6, 1, 8], [7, 5, 0], [2, 9, 4]])) # returns 3 
print (complete_the_square ([[6, 1, 8], [7, 5, 3], [2, 9, 0]])) # returns 4 