def leapYear():
    Year = int(input("Enter a year : "))
    if Year%4 == 0 and Year%100 != 0 or Year%400 == 0:
        return f'{Year} is a leap Year'
    else: return f'{Year} is not a leap Year'
print(leapYear())