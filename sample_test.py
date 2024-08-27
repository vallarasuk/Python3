class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def search_by_title(self, title):
        found = []
        for book in self.books:
            if title.lower() in book.title.lower():
                found.append(book)
        
        if not found:
            print("No books found with that title.")
        else:
            for book in found:
                print(book)


# Sample Usage
if __name__ == "__main__":
    # Create a library instance
    my_library = Library()

    # Create some book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book3 = Book("1984", "George Orwell Lee")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book4 = Book("vallarasuk d", "same")

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.add_book(book4)
    
 
 
    print("\nSearching for books with title 'vallarasuk':")
    my_library.search_by_title("vallarasuk")
