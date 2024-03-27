import re

with open("somethingie") as f:
    file = f.read()
filies = re.search("[xy]*x[xy][xy][xy]",file)
print(filies)