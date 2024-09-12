import re

with open("1_main.txt") as f :
    data = f.readlines()
print(data)
values = []
for line in data:
    cipari = re.findall("\d",line)
    print(cipari, "šie ir atrastie cipari")
    abi_cipari = cipari[0]+cipari[-1]
    abi_cipari = int(abi_cipari)
    print(abi_cipari)
    values.append(abi_cipari)
rezultāts = 0
for value in values:
    rezultāts += value
print(rezultāts)