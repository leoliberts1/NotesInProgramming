import re
with open("example.txt","r") as f:
    data = f.read()
print(data)

#First off I shoul just look for the numbers and If they are found I should save them and get their location
#in the list so I can check everything around them
def finding_num(line):
    numbers = re.findall("\d+",line)
    index = 0
    number_index = 0
    actual_numbers = []


for line in data:
    numerical_values = finding_num(line)
    print(numerical_values)

        #I have all the numbers in the line now and their indexes



