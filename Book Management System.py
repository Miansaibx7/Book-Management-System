import json
from datetime import datetime
# title: The title of the book (string)
# author: The author's name (string)
# isbn: International Standard Book Number (string or int)
# publisher: Publisher's name (string)
# year: Year of publication (int)
# price: Price of the book (float)

def discount_decorator(percent):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            discount_amount = self.price * (percent / 100)
            self.price -= discount_amount
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

class Library:
    def __init__(self,title,author,isbn,publisher,year,price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.year = year
        self.price = price
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Book discount method but we use a decorators
    @discount_decorator(10)
    def apply_discount(self):
       print(f"New price after discount: {self.price}")

    
    def update_price(self, new_price):
        self.price = new_price

# Create a dictionary for add a book
    def dict_new(self):
         return {  
           "Title"     : self.title,
           "Author"    : self.author,
           "Isbn"      : self.isbn,
           "Publisher" : self.publisher,
           "Year"      : self.year,
           "Price"     : self.price,
           "Created_at": self.created_at,
        }
    
# Create a class for stor new book 
class StoreBook:
    def __init__(self):  # for that intial create a empty List
        self.books = []
    # Make a Method to add a book
    def add_book(self,title,author,isbn,publisher,year,price):
        add_new_book = Library(title,author,isbn,publisher,year,price)
        self.books.append(add_new_book)
        print("Book added successfully")

    # Create a Method to show a book list
    def show(self):
        if not self.books:
            print("No books available. Search for another book.")
            return
        for idx,book in enumerate(self.books,start=1):
            print(f"\nBook {idx}")
            for key,value in book.dict_new().items():
                print(f"{key}: {value}")

    # Create a Method to Save the data of the books
class SaveFile:
    def file_save(self,books,filename = "Books.json"):
        with open (filename,"w") as f:
            json.dump([b.dict_new() for b in books],f, indent=4)
            print(f"All books saved to {filename}")

store = StoreBook()
store.add_book("Python 101", "Ali Khan", "12345", "TechPress", 2023,1500.0)
store.add_book("The Secrets of Quantum Code","Dr. Evelyn Hart",9781234567890,"NovaTech Press",2021,4000)

# Apply discount to all books
for book in store.books:
    book.apply_discount()

store.show()

saver = SaveFile()
saver.file_save(store.books)