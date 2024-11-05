class Library():
    def __init__(self):
        self.books = []
        self.checked_out = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        self.books.remove(book)
    
    def check_in(self, book):
        self.books.append(book)
        self.checked_out.remove(book)

    def check_out(self, book):
        self.checked_out.append(book)
        self.books.remove(book)
    
    def list_book_titles(self):
        print("Printing current list of book titles in the library:")
        for book in self.books:
            print(book.title)
    
    def list_checked_out(self):
        print("Printing current lsit of checked out book titles:")
        for book in self.checked_out:
            print(book.title)
    
class Book():
    def __init__(self, title, author, num_pages) -> None:
        self.title = title
        self.author = author
        self.num_pages = num_pages

book_1 = Book('The Great Gatsby', 'F. Scott Fitzgerald', 300)
book_2 = Book('Ulysses', 'James Joyce', 250)
book_3 = Book('The Catcher in The Rye', 'J. D. Sallinger', 275)
book_4 = Book('To Kill a Mockingbird', 'Harper Lee', 225)
library = Library()

books = [book_1, book_2, book_3, book_4]

for book in books:
    library.add_book(book)

library.list_book_titles()
library.check_out(book_2)
library.list_checked_out()