list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
final=[]
for i in list1:
     final.append(i + list2[list1.index(i)])
print(final)