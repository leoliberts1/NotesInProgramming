class ShopingCart:
    def __init__(self,Name,Date):
        self.name = Name
        self.dateOfPurchase = Date
        self.elements = {}
    def AddProduct(self,name,price):
        self.elements.update({name:price})
        print(name," has been added")
    def RemoveProduct(self,name):
        self.elements.pop(name)
        print(name,"has been removed")
    def CalculatePrice(self):
        price = 0
        for element in self.elements:
            price+=self.elements.get(element)
        return print(price)