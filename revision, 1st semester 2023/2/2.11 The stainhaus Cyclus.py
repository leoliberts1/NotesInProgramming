#Get the number first
#make a while loop that counts the number of 1's or 145's
#get a for loop goint in the while loop that adds up the squares of all the numbers
# print the number gotten using end=
#restart the proces with the number gotten from the for loop
def Steinhaus():
    start = int(input("Enter a 4 digit number : "))
    counter = 0
    print("Sequence : ",end="")
    while counter <2:
        new = 0
        for element in str(start):
            new += int(element)**2
        start = new
        print(start,end=",")
        if start == 1 or start == 145:
            counter +=1
Steinhaus()