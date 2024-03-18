def wordcounter(fileName,Length, n):

    import re
    with open(fileName) as f1:
        text = f1.read()
    print(type(text))
    arg = text.replace("\n"," ")
    arg = re.sub(r'[^\w]'," ",arg)
    arg = arg.split(" ")
    worddictionary = {}
    wordGoodLength = []
    for element in arg:
        if len(element) == Length:
            wordGoodLength.append(element)
    print(wordGoodLength)
    for Arg in wordGoodLength:
        if Arg not in worddictionary:
            worddictionary[Arg] = 1
        else :worddictionary[Arg] +=1
    print(worddictionary)
    sortedWords = sorted(worddictionary.items() , key = lambda x:x[1],reverse=True)
    sortedWords = dict(sortedWords)
    print(sortedWords)
    sortedWords = list(sortedWords)
    print(sortedWords)
    print(sortedWords[n-1])
    return
wordcounter("text", 3,1)

