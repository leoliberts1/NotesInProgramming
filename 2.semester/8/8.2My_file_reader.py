
class this_file_reader():
    def __init__(self):
        self.file = __file__
    def __enter__(self):
        self.file = open(self.file)
        return self.file
    def __exit__(self,exception,value,trace):
        self.file.close()

with this_file_reader() as fm:
    print (fm.read())
#file is closed when execution reaches this line
print (fm.closed)