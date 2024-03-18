

def csvfilecomparer(file1,file2):
    import csv
    with open(file1, "r") as f:
        data = list(csv.reader(f,delimiter=";"))
    print(data)
    with open(file2, "r") as f:
        data2 = list(csv.reader(f,delimiter=";"))
    print(data2)
    commondict = {"same":None,"different":None}

    for element in data:
        if data.index(element) == 0: continue
        #elif set(element) == set(data2[data.index(element)]):
        #    commondict.update({"same":commondict.get("same")+[(data2[data.index(element)][0])]})
        #elif set(element) != set(data2[data.index(element)]):
        #    commondict.update({"different":commondict.get("different") + [(data2[data.index(element)][0])]})
        same = []
        something = data2[data.index(element)]
        for arg in element:
            if arg in data2[data.index(element)]:
                same.append(1)
            else: same.append(2)
        if len(same) == same.count(1):
            if commondict.get("same") == None:
                commondict.update({"same":[element[0]]})
            else:
                commondict.update({"same":commondict.get("same") + [element[0]]})
        else:
            if commondict.get("different") == None:
                print(element[0])
                commondict.update({"different":[element[0]]})
            else: commondict.update({"different":commondict.get("different")+[element[0]]})

    return print(commondict)




csvfilecomparer("file1.csv","file2.csv")