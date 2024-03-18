with open("numbers.txt") as f1:
    text = f1.readlines()
text2=[]
for i in text:
    text2.append(i.replace("\n",""))
print(text2)
for i in text2:
    for n in text2:
        for g in text2:
            if (int(i)+int(n)+ int(g)) == 2020:
                print(int(i)*int(n)*int(g))