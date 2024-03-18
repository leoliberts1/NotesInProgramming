#print("Current hand: ", end = '')
def JoinStrings():
    Something = str(input("Write something "))
    if len(Something) < 2:
        return "empty string"
    else :return "".join([Something[0:2],Something[-2:]])
print(JoinStrings())