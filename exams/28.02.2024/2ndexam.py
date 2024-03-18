with open("randome_ums.txt", "r") as f:
    data = f.read()
    listt = []
    diff = []
    res = 0
    for line in data.split("\n"):
        listt2 = []
        for number in line.split(" "):
            listt2.append(number)
        listt.append(listt2)
    for row in listt:
        try:
            max_value = max(row, key=lambda x: int(x))
            min_value = min(row, key=lambda x: int(x))
            diff.append(int(max_value) - int(min_value))
        except ValueError:
            pass
    for difference in diff:
        res += difference
    print(res)

d = {"teacher": ["Mark", "James", "Sandy"],
     "police":  ["James", "Mary", "Danny"],
     "gardener":["Mark", "Sandy", "James"] }

def find_roles(mydict, name):
    res = []
    for k,v in mydict.items():
        if name in v:
            res.append(k)
    return res
print(find_roles(d, "James"))

words = ["abc", "cat", "bananna", "abcba", "121", "palindromes", "dollar", "abcdcba", "semordnilap", "tac", "stressed", "desserts"]
res = []
listt = []
for word in words:
    for word2 in words:
      if word == word2[::-1] and word not in listt and word2 not in listt:
            listt.append(word)
            res.append((word, word2))
print(res)

my_dict = {'a b c': [2, 3, 5],
'b d e': [1, 8, 4],
'c f g': [9, 0, 1],
'bd e': [100, 10, 1]}
res = {}
for k, v in my_dict.items():
    b = ''
    for ch in k:
        if ch == " ":
            pass
        else:
            b = b + ch
    k = b
    res.update({k:v})
print(res)






