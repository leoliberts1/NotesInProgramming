


cart = ["milk", "sugar", "milk", "x3", "sugar", "beer", "x12", "bread", "milk", "butter", "x2", "salad", "x3", "juice", "sugar", "x2", "juice", "butter", "sugar", "flour"]
pricelist = {"milk":1.3, "sugar":1.6, "beer":1.25, "bread":2.6, "butter":1.99, "salad":0.89, "flour":1.2, "juice":1.2}

def printBill(cart,prices):
    cost = 0
    index = 0
    for element in cart:
        if element[0] == "x":
            index+=1
            continue
        elif index == len(cart)-1:
            cost+= prices.get(element)
            index+=1
            continue
        else:
            if cart[index+1][0] == "x":
                cost+= prices.get(element)*float(cart[index+1][1::])
            else:cost+= prices.get(element)
            index+=1
    return print(cost)



printBill(cart, pricelist) #Returns : 44.34