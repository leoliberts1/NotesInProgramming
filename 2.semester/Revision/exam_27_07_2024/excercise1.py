import json
class Book():
    def __init__(self,id):
        self.id = id
        self.url = None
        self.title = None
        self.upc = None
        self.product_type = None
        self.price_excl_tax = None
        self.price_incl_tax = None
        self.tax = None
        self.price = None
        self.availability = None
        self.num_reviews = None
        self.stars =None
        self.category = None
        self.description = None


class Library():
    def __init__(self,json_books):
        self.books = []
        with open(json_books, "r") as f:
            data = json.load(f)
            #print(data)
            for book in data:
                index = 0

                for element in book:
                    if index == 0 :
                        b = Book(book[f'{element}'])
                    else:

                        b.element = book[f"{element}"]
                        print(b.element,"I should get a value from the book object here")
                        print(element,"this is the element itself")
                        print(book[f"{element}"],"this is what I get when I get it out from the book")
                    index +=1
                self.books.append(b)
    def raiting(self,n):
        books_in_question = []
        for book in self.books:
            if book.stars == n:
                books_in_question.append(book)
        return books_in_question

L = Library("Books.json")

print(L.raiting(1))