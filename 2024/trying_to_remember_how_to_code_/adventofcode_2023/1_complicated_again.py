import re

with open("1_main.txt") as f :
    data = f.readlines()
print(data)
ciparu_pārveidotājs = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
def pārveidot_ciparos(izvēlētie_cipari):
    normalizēti_cipari = []
    for index in izvēlētie_cipari:
        if ciparu_pārveidotājs.get(index):
            normalizēti_cipari.append(str(ciparu_pārveidotājs.get(index)))
        else : normalizēti_cipari.append(index)
    return "".join(normalizēti_cipari[0]+normalizēti_cipari[1])
rezultāts = 0
atrastie_cipari = []
for line in data:
    line = line.lower()
    cipari = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine",line)
    print(len(cipari))
    izvēlētie_cipari = [cipari[0],cipari[-1]]
    #print(izvēlētie_cipari)
    gala_cipars = pārveidot_ciparos(izvēlētie_cipari)
    #print(gala_cipars)
    rezultāts += int(gala_cipars)
print(rezultāts)
