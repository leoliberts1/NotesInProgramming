class Book ():
    def __init__(self, name,authors):
        self.name = name
        self.authors = authors
        self.index = -1
    def __repr__(self):
        return self.name
    def __iter__(self):
        return self
    def __next__(self):

        self.index +=1
        if self.index < len(self.authors):
            return self.authors[self.index]
        else :
            raise StopIteration
class BookIterator():
    def __init__(self,books):
        self.books = books
        self.current = -1

    def __iter__(self):
        return self
    def __next__(self):
        self.current +=1
        if self.current >= len(self.books):
            raise StopIteration
        return self.books[self.current]



class Library():
    def __init__(self):
        self.__books = []
    def __iter__(self):

        return BookIterator(self.__books)
    def addBook(self,book):
        self.__books.append(book)





library = Library()
library.addBook(Book("Huckleberry Finn",["Mark Twain"]))
library.addBook(Book("Tom Sawyer",["Mark Twain"]))
library.addBook(Book("Animal Farm",["George Orwel"]))
library.addBook(Book("Lord of the flies",["William Golding"]))
for book in library:
    print(book)
