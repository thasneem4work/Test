from bookclass import book

def info(book):
    print(f"ISBN No:{book.isbn}, Book Title:{book.title}, Book Format{book.format}, Subject:{book.subject}, Rental Price:{book.rental}, Copies Availble:{book.copies}")


class Bookfunction:
    def __init__(self):
        self.booklist=[]
        self.__data()

    def __data(self):
        book1= book(isbn="ISBN1234", title="The Solar System", format="Hardcover", subject="Science", rental=15.00, copies=5)
        book2= book(isbn="ISBN9876", title="Types of Animal Species", format="Paperback", subject="Science", rental=10.00, copies=8)
        book3= book(isbn="ISBN1290", title="Second World War",format="Hardcover", subject="History", rental=12.50, copies=1)
        self.booklist.append(book1)
        self.booklist.append(book2)
        self.booklist.append(book3)

    def add(self):
        __isbn = input("Please enter ISBN No: ").strip().upper()
        __title= input("Enter Title: ")
        __format= input("Enter Format: ")
        __subject= input("Enter subject: ")
        __rental=input("Enter rental per day: ")
        __copies=input("Enter no of copies: ")

        bookx= book(isbn=__isbn, title=__title, format=__format, subject=__subject, rental=__rental, copies=__copies )
        self.booklist.append(bookx)
        print(f"A book is added successfully")

    def remove(self):
        __isbn = input("Please enter ISBN No to be removed: ")
        matched_data= list(x for x in self.booklist if x.isbn==__isbn)
        for x in matched_data:
            self.booklist.remove(x)
            print("book removed successfully.")

    def lend(self):
        __isbn = input("Please enter ISBN No: ")
        __copies= input("Enter no of copies lent: ")
        matched_data= list(x for x in self.booklist if x.isbn==__isbn)
        for x in matched_data:
            x.copies-=__copies
            print("Book lent successfully")

    def receive(self):
        __isbn = input("Please enter ISBN No: ")
        __copies= input("Enter no of copies recieved: ")
        matched_data= list(x for x in self.booklist if x.isbn==__isbn)
        for x in matched_data:
            x.copies+=__copies
            print("Book received successfully")

    def display_all(self):        
        for x in self.booklist:
            info(book=x)

    def dis_available(self):
        matched_data= list(x for x in self.booklist if x.copies>0)
        for x in matched_data:
            info(book=x)

    def dis_unavailable(self):
        matched_data= list(x for x in self.booklist if x.copies==0)
        for x in matched_data:
            info(book=x)
