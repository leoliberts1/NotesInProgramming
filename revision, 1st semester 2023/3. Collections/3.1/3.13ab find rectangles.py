import itertools
L = [(10,20), (10,30), (10,40), (20,20), (20,30), (20,50), (30, 10)]
itered = itertools.permutations(L,4)
rectangles = []
#for a rectangle to be real it has to have two points on the same y axis(second nr)
#but different x axis, and the other hand the points above them/bellow have to have
#the same x axis, first number the same but the y is different
for argument in itered:
    print(argument)
    #I will have the first two elements be the bottom points that have the same y axis but
    #different x, I will look then to the other two elements if their y axis are the same
    #and if for each of them the x axis is the same respectively to the other points
    if argument[0][1] == argument[1][1] and argument[0][0] != argument[1][0]:
        if argument[0][0] == argument[2][0] and argument[0][1] != argument[2][1]:
            if argument[1][0] == argument[3][0] and argument[1][1] != argument[3][1] and argument[2][1] == argument[3][1]:
                if argument not in rectangles:
                    rectangles.append(argument)
print(rectangles)