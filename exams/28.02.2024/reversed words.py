words = ["abc", "cat", "bananna", "abcba", "121", "palindromes", "dollar", "abcdcba", "semordnilap", "tac", "stressed", "desserts"]
def reversedw(words):
    revWords = []
    for word in words:
        for i in words:
            if word == i[::-1] and word != i:
                if (word,i) not in revWords and (i,word) not in revWords:
                    revWords.append((word,i))
    return revWords

print(reversedw(words))
#should return [("cat", "tac"),("palindromes", "semordnilap"), ("stressed", "desserts")]