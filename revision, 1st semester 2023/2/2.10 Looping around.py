def looping_around():
    start = int(input("Enter the starting number"))
    end = int(input("Enter the ending number"))
    summ = 0
    for arg in range(start,end):
        summ += arg**2
    return(print(summ))

looping_around()