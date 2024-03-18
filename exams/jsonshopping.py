

#figure out the price the customer has to pay for their groceries
def shopping(shop,customer):
    import json
    with open(shop) as f:
        prices = json.load(f)
    print(prices)
    with open(customer) as f1:
        cart = json.load(f1)
    print(cart)
    for item in cart :

shopping("shop.json","customer1.json")