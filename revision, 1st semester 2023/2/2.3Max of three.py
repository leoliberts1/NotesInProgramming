def maxOfThree():
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    num3 = int(input("Enter a number"))
    num_list = []
    num_list.extend([num1,num2,num3])
    return max(num_list)
print(maxOfThree())