# Something I see a lot, but you SHOULDN'T DO


class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"BookShelf with {self.quantity} books."


shelf = BookShelf(300)


class Book(BookShelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name


# This makes no sense, because now you need to pass `quantity` to a single book:

book = Book("Harry Potter", 120)
print(book)  # What?

# -- Composition over inheritance here --

# Inheritance: "A Book is a BookShelf"
# Composition: "A BookShelf has many Books"


class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name


book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)
