def CraftsmanBill():
    Hours = int(input("How many hours worked?"))
    cableM = int(input("How many meters were laid?"))
    cost = 0
    if cableM % 500 == 0 :
        cost+= cableM//500*1000
    else: cost+= cableM//500*1000+(cableM-cableM//500)*3
    if Hours > 40:
        cost+= 40*50 + (Hours-40)*100
    else : cost += Hours*50
    return f' This week has costed  {cost} euro'
print(CraftsmanBill())