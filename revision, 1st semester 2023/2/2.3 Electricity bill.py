def ElectricityBill():
    Units = int(input("Enter the number of electrecity units used "))
    if Units < 51 :
        return f'Price you have to pay is {Units*0.5}'
    elif Units < 151:
        return f'Price you have to pay is {50*0.5 +(Units-50)*0.75}'
    elif Units <251:
        return f'Price you have to pay is {50 * 0.5 + 100 * 0.75 + (Units-150)*1.2}'
    else: return f'Price you have to pay is {(50 * 0.5 + 100 * 0.75 + 100*1.2+ (Units-250)*1.5)*1.2}'

print(ElectricityBill())