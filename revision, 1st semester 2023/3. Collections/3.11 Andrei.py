import re
formula=input("Enter Molecular Formula in correct notation: ")
pieces = re.findall("[A-Z][a-z]?|[0-9]+", formula)
dictionary = {}
for i in range(len(pieces) - 1):
    if i != len(pieces) - 2:
        if pieces[i].isalpha():
            if pieces[i + 1].isalpha():
                dictionary[pieces[i]] = 1

            else:
                dictionary[pieces[i]] = pieces[i + 1]
    elif pieces[i + 1].isalpha():
        dictionary[pieces[i + 1]] = 1
    else:
        dictionary[pieces[i]] = pieces[i + 1]

print("Formula:", "".join(pieces), end="\n")
for i in range(len("".join(pieces)) + 9):
    print("=", end="")
print("")
for key, val in dictionary.items():
    print(key, end="")
    for i in range(len("".join(pieces)) - (len(key)) - (len(str(val))) + 9):
        print(" ", end="")
    print(val)