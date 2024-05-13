for c in "Happy Birthday":
    print(c)
print("Beigas")
y = iter("Happy Birthday")
print(y)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

print("\n <------Our iterator------->")
class Myrange():
    def __init__(self,start=0,end=0,step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = self.start - self.step
    def __iter__(self):
        return self
    def __next__(self):
        self.current = self.current + self.step
        if self.current >= self.end :
            raise StopIteration
        return self.current

for c in Myrange(0,10,3):
    print(c)
