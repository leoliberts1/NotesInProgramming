a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
final = []
for value in a:
    for value2 in b:
        if value == value2 and value not in final:
            final.append(value)
print(final)