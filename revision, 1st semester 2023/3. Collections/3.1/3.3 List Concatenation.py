list1 = ["M","na","i","Ke"]
list2 = ["y","me","s","lly"]

list_full = []
for element in list1:
    for element2 in list2:
        if list1.index(element) == list2.index(element2) and (element+element2) not in list_full:
            list_full.append(element+element2)
print(list_full)