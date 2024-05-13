#The sequence goes as follows: 1, 2, 3, 4, 32, 123, 43, 2123, 432, 1234, 32123, ...

class SequenceGenerator():
    #1234321 is the sequence base
    #and it goes
    #123432 1 23 4 32 1 23 4
    #and I somehow have to break it into parts such that
    #All the numbers individually counted up make the index of that list

    def __init__(self,n=1):
        self.n = n
        self.current =  1
        self.growing = True
        self.number = 1
    def generate(self):
        while True:
            yield self.current
            #print(self.current)
            if self.growing == True and self.current < 4:
                self.current +=1
            elif self.current == 4:
                self.growing = False
                self.current -=1
            elif self.growing == False and self.current > 1:
                self.current -=1
            elif self.current == 1:
                self.growing = True
                self.current +=1
    def __iter__(self):
        return self
    def __next__(self):
        while self.number >= self.n:
            hope = []
            def getNr(list):
                numbers = 0
                for element in list:
                    numbers += element
                return numbers
            number = getNr(hope)
            while number != self.number:
                hope.append(self.generate())
                number = getNr(hope)
            yield hope
            self.number +=1
        raise StopIteration





gen = SequenceGenerator()


for x in range (10): # print 10 numbers
    print (gen.__next__())
gen = SequenceGenerator(10)
for x in gen:
    print (x)