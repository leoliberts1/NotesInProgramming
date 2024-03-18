def censor(arg):
    words = arg.split(" ")
    print(words)
    censored = []
    for i in words:
        if len(i) < 5: censored.append(i)
        else: censored.append("*"*len(i))
    return print(" ".join(censored))
censor("The code is fourty")
censor("Two plus three is five")
censor("aaaa aaaaa 1234 12345")