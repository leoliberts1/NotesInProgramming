list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

list2 = ["h", "i", "j"]

print(list1[2][1][2][1])
list1[2][1][2].extend(list2)
print(list1)