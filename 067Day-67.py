# Library Management Software in Python!!

class Library:
    def __init__(self):
        self.Books = []
        self.count = 0
    def addBook(self,Book):
        self.Books.append(Book)
        self.count  = len(self.Books)
    def ShowInfo(self):
        print(f"{self.count} Books and name of the books is/are:")
        for Book in self.Books:
            print(Book)

L1 = Library()
L1.addBook("SambhavBook")
L1.addBook("Kalbharav")
L1.ShowInfo()
