L = [(10,20), (10,30), (10,40), (20,20), (20,30), (20,50), (30, 10)]

Lsorted = sorted(L)
print(Lsorted)





'''
lowPoints = []
highpoints = []

rectangle = []
rectangleList = []


for element in L:
    for element2 in L:
        if element!= element2:
            if element[0] == element2[0] and element[-1] != element2[-1] and len(lowPoints)==0:
                    lowPoints.append(element)
                    lowPoints.append(element2)

            elif len(lowPoints)!=0:
                for element3 in L:

                    for element4 in L:
                        if element3[1] == element4[1] and element3[0] != element4[0]:
                            if element3[0] == element[0] and element3[1] != element[1] and element4[0] ==element2[0]:
                                highpoints.append(element3)
                                highpoints.append(element4)

                                rectangle.extend(highpoints)
                                rectangle.extend(lowPoints)
                                if rectangle not in rectangleList:
                                    rectangleList.append(rectangle)
                                lowPoints = []
                                highpoints = []
                                rectangle = []
print(rectangleList)
'''

