class Library:
    def __init__(self, name, book, quantity):
        self.name = name #self is used to store values inside the object
        self.book = book
        self.quantity = quantity

    def display_library(self):
        print("Library Name:", self.name)
        print("Available Book in library:", self.book)
        print("Quantity Available in library:", self.quantity )

name = input("Enter library name: ")
book = input("Enter book name: ")
quantity = int(input("Enter book quantity: "))

lib = Library(name, book, quantity) #creating object
lib.display_library()