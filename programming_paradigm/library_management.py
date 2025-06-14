class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        

class Library:
    def __init__(self):
        self._books = []
    
    
    def add_book(self,book):
        self._books.append(book)
        print(f"Added {book.title} by {book.author} to the library.")
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = True
                self._books.remove(book)
                print(f"Checked out {book.title} by {book.author}.")
                return True
            
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out==True: 
                book._is_checked_out = False
                self._books.append(book)
                return True
            return False
    
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title}")   