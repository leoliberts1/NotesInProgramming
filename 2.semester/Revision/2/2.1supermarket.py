import random

class Article():
    def __init__(self,name,category):
        self.name = name
        self.price = None
        self.category = category
    def setPrice(self,price):
        self.price = price
    def applyDiscount(self,discount):
        self.price = self.price *(1-discount)
    def __repr__(self):
        return self.name, self.price
class Supermarket():
    def __init__(self,name):
        self.name = name
        self.articles = []
    def addArticle(self,article,count):
        self.articles.append([article,count])
    def discountAktion(self,discount,category):
        for article in self.articles:
            if article[0].category == category:
                article[0].applyDiscount(discount)
    def __repr__(self):
        text = ""
        for element in self.articles:
            text += element[0].name +" "+ str(element[0].price) +" euro \n"
        return text



a1 = Article ("Fresh Soap 200g", "hygiene")
a2 = Article ("Rose Shampoo 200 ml", "hygiene")
a3 = Article ("Coal Toothpaste 50g", "hygiene")
a4 = Article ("Mango 1 Pc", "fruits")
a5 = Article ("Orange 1 Kg", "fruits")
a6 = Article ("Apple 1 Kg", "fruits")
mk = Supermarket("Happymarket")
for a in (a1, a2, a3, a4, a5, a6):
    a.setPrice( random.randint(1,320))
    mk.addArticle(a,random.randint(1,40))

print (mk) # prints all items in supermarket
mk.discountAktion(0.25, "fruits" ) # 25% discount on fruits
print (mk) # prints all items in supermarket