import re

with open("1_main.txt") as f :
    data = f.readlines()
print(data)
values = []
texta_cipari = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
def transform_to_int(number_list):
    new_number_list = []
    for element in number_list:
        try:
            element = int(element)
        except:
            element = texta_cipari.get(element)
        finally: new_number_list.append(element)
    return new_number_list
def uztaisīt_ciparu(divi_cipari):
    cipars = ""
    for element in divi_cipari:
        cipars += str(element)
    cipars = int(cipars)
    return cipars


for line in data:
    cipari = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine",line)
    print(cipari, "šie ir atrastie cipari")
    abi_cipari = [cipari[0],cipari[-1]]
    abi_cipari = transform_to_int(abi_cipari)
    print(abi_cipari,"šie ir abi cipari")
    nummurs = uztaisīt_ciparu(abi_cipari)
    print(nummurs,"šis ir nummurs kas sanāk")
    values.append(nummurs)
rezultāts = 0
for value in values:
    print(value)
    rezultāts += value
print(rezultāts,"šis ir rezultāts")