def filestripper(file,word):
    with open(file) as f:
        data = f.read()
    data2 = []
    data = data.split(" ")
    for element in data:
        element = element.replace("\n", "")
        if element != word:
            data2.append(element)
    with open(file, "w") as f:
        f.write(" ".join(data2))
filestripper("1something","hopefully")

###################################################

def filecomparer(file1,file2):
    with open(file1) as f:
        data = f.readlines()
    with open(file2) as f:
        data2 = f.readlines()
    common = []
    for line in data:
        for line2 in data2:
            if line == line2 and line not in common:
                common.append(line)
    return common
filecomparer()