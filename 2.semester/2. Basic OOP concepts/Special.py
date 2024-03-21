class Fruit:
    pass
class Apple(Fruit):
    def __init__(self,stemLength):
        self.stemLength = stemLength
class Orange(Fruit):
    def __init__(self,pulp):
        self.pulp = pulp
def special(list1):
    if "apple" in list1:
        return Apple(2)
    else: return Orange("tasty")
x = special(["Apple","Orange"])
#print(x.stemLength)
attrList = ["pulp","color"]
if isinstance(x,Apple):
    print(x.stemLength)
if isinstance(x,Orange):
    print(x.pulp)
if hasattr(x,"pulp"):
    for atribute in attrList:
        setattr(x,atribute,43)
    print(x.pulp)
print(x.__dict__)
