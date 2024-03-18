import random
class Supermarket:
    def __init__(self, name):
        self.name = name
        self.articles = []
    def addArticle(self,article,value):
        self.articles.append([article,value])
    def discountAktion(self,discount,type):
        for article in self.articles:
            if article[0].type == type:
                article[0].setPrice(article[0].price-article[0].price*discount)
    def __str__(self):
        largestr = ""
        for article in self.articles:
            #print(type(article[0]))
            largestr+= str(article[0])
            largestr+= "\n"
        return largestr

class Article:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.price = None
    def setPrice(self,value):
        self.price = value
    def __str__(self):
        return self.name + " "+ self.type + " " + str(self.price)


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