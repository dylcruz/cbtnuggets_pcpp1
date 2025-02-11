class Library():
    def __init__(self, books):
        self.books = books
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

    def __iter__(self):
        return BookIterator(self.books, self.checked_out)
    
    def __contains__(self, value):
        if (isinstance(value, str)):
            for book in self.books:
                if value == book.title:
                    print(f'Yes, our library contains the book {value}')
                    return True
            for book in self.checked_out:
                if value == book.title:
                    print(f'Yes, our library contains the book {value}. However it is currently checked out.')
                    return True
            print(f'Sorry, our library does not contain the book {value}')
        else:
            return NotImplemented
        
class BookIterator():
    def __init__(self, books, checked_out):
        self._books = books
        self._checked_out = checked_out
        self._current_index = 0
        self._current_index_co = 0
    
    def __next__(self):
        if self._current_index >= len(self._books):
            if self._current_index_co >= len(self._checked_out):
                raise StopIteration
            current_element = self._checked_out[self._current_index_co]
            self._current_index_co += 1
            return current_element
        
        current_element = self._books[self._current_index]
        self._current_index += 1
        return current_element

class Book():
    def __init__(self, title, author, num_pages) -> None:
        self.title = title
        self.author = author
        self.num_pages = num_pages

book_1 = Book('The Great Gatsby', 'F. Scott Fitzgerald', 300)
book_2 = Book('Ulysses', 'James Joyce', 250)
book_3 = Book('The Catcher in The Rye', 'J. D. Sallinger', 275)
book_4 = Book('To Kill a Mockingbird', 'Harper Lee', 225)
library = Library([book_1, book_2, book_3, book_4])

library.check_out(book_1)

for book in library:
    print(book.title)

print('The Great Gatsby' in library)