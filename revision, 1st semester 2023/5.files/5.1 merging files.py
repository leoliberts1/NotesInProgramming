def filemerger(file1,file2):
    with open( file1) as f:
        data = f.read()
    with open(file2) as f:
        data2 = f.read()
    data += data2
    with open(file1+file2, "w") as f:
        f.write(data)
    return print(file1+file2)


file1 = "1something"
file2 = "2something"

filemerger(file1, file2)