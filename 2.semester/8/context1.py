class mycontext():
    def __init__ (self, p):
        self.p = p
    def __enter__(self):
        print ("Create Context")
        return "c-object"
    def __exit__(self, exception, value, trace):
        print ("Clear Context")





with mycontext("") as c:
    print (c,"in the context")
print ("after the context", c)


class myfileOpener():
    def __init__(self,filename):
        self.name = filename
        self.file = None
    def __enter__(self):
        self.file = open(self.name)
        return self.file
    def __exit__(self,exception,value,trace):
        self.file.close()
with myfileOpener("") as myself:
    print(myself.read())
print("-------------------------")
