

class FibSequence():
    def __init__(self,n):
        self.n = n
        self.count = 0
        self.previous = 1
        self.previous2 = 0
    def __iter__(self):
        return self
    def __next__(self):
        x = self.previous + self.previous2
        self.previous2 = self.previous
        self.previous = x
        self.count += 1
        if self.count >= self.n:
            raise StopIteration
        return x
        #1, 1, 2, 3, 5, 8, 13, 21, 34, ...


fib = FibSequence(10)
print (next (fib) )
print (next (fib) )
print (next (fib) )
print("<=================>")

for c in FibSequence(700):
    print (c)


