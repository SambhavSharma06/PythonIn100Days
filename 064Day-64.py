#Library Management System in Python!!

class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in library:")
            for book in self.books:
                print(book)

    def show_no_of_books(self):
        print("Total books:", self.no_of_books)


lib = Library()

while True:
    print("\n1. Add Book")
    print("2. Show All Books")
    print("3. Show Number of Books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        lib.add_book(name)
        print("Book added successfully.")

    elif choice == "2":
        lib.show_books()

    elif choice == "3":
        lib.show_no_of_books()
        print("Using len():", len(lib.books))

    elif choice == "4":
        print("Program ended. Books are not saved.")
        break

    else:
        print("Invalid choice. Try again.")
