class Newspaper():
    count = 0
    Publisher = "IMC"
    def __init__(self,name):
        self.name = name
        Newspaper.count+=1
    def ReadNewspaper(self):
        print(self.name)
    @classmethod
    def getNepspaperCount(clz):
        return Newspaper.count
n1 = Newspaper("Times")
#print(n1._Newspaper__name)
#print(n1.__dict__)
print(Newspaper.count)
n2 = Newspaper("Washington")
n3 = Newspaper("Post")
Newspaper("diena")
n1.ReadNewspaper()
n2.ReadNewspaper()
Newspaper("diena")
Newspaper("diena")
Newspaper("diena")
Newspaper("diena")
Newspaper("diena")
print(Newspaper.count)
print(Newspaper.getNepspaperCount())