def findFirstOccurrence(sentence, words):
    return min(words, key=lambda word: sentence.find(word) if word in sentence else len(sentence))

def findLastOccurrence(sentence, words):
    return max(words, key=lambda word: sentence.rfind(word) if word in sentence else -1)



with (open("1st.txt") as f):
    data = f.readlines()

wNum = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine","1","2","3","4","5","6","7","8","9"]
num = []
for i in data:
    num.append([findFirstOccurrence(i, wNum), findLastOccurrence(i, wNum)])

# Converting sting to a number
print(len(num))
for i in range(len(num)):
    for j in range(len(num[i])):
        if num[i][j] == "one": k = "1"
        elif num[i][j] == "two": k = '2'
        elif num[i][j] == "three": k = '3'
        elif num[i][j] == "four": k = '4'
        elif num[i][j] == "five": k = '5'
        elif num[i][j] == "six": k = '6'
        elif num[i][j] == "seven": k = '7'
        elif num[i][j] == "eight": k = '8'
        elif num[i][j] == "nine": k = '9'
        else: k = num[i][j]
        num[i][j] = k

comb_list = []
for i in num:
    comb = i[0] + i[1]
    comb_list.append(comb)
print(comb_list)

cNum = []
for i in comb_list:
    if len(i) > 1:
        s = i[0] + i[-1]
        cNum.append(s)
    else:
        cNum.append(i+i)
num = []
for i in cNum:
    num.append(int(i))


print(sum(num))