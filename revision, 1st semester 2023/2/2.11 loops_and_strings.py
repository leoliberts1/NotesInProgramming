def isisogram():
    word = str(input("Enter word : "))
    word = word.lower()
    #print(word)
    word2 = set(word)
    #print(word,word2)
    if len(word) == len(word2):
        return(print("Is an isogram"))
    else: return (print("Not an isogram"))
isisogram()
somth = "Algorism"
print(len(set(somth)))