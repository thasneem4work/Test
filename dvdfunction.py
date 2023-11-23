from dvdclass import dvd

def info(dvd):
    print(f"DVD No:{dvd.dvdno}, CD Title:{dvd.title}, Subject:{dvd.subject}, Rental Price:{dvd.rental}, Copies Availble:{dvd.copies}")


class dvdfunction:
    def __init__(self):
        self.dvdlist=[]
        self.__data()

    def __data(self):
        dvd1= dvd(dvdno=10, title="Bairth of Solar System",subject="Astronomy", rental=2.50, copies=10)
        dvd2= dvd(dvdno=11, title="pythagoras Theorem",subject="Math", rental=1.00, copies=50)
        
        self.dvdlist.append(dvd1)
        self.dvdlist.append(dvd2)

    def add(self):
        __dvdno = input("Please enter DVD No: ").strip().upper()
        __title= input("Enter Title: ")
        __subject= input("Enter subject: ")
        __rental=input("Enter rental per day: ")
        __copies=input("Enter no of copies: ")

        dvdx = dvd(dvdno=__dvdno, title=__title, subject=__subject, rental=__rental, copies=__copies )
        self.dvdlist.append(dvdx)
        print(f"A DVD is added successfully")

    def remove(self):
        __dvdno = input("Please enter DVD No to be removed: ")
        matched_data= list(x for x in self.dvdlist if x.dvdno==__dvdno)
        for x in matched_data:
            self.cdlist.remove(x)
            print("CD removed successfully.")

    def lend(self):
        __dvdno = input("Please enter CD No: ")
        __copies= input("Enter no of copies lent: ")
        matched_data= list(x for x in self.dvdlist if x.dvdno==__dvdno)
        for x in matched_data:
            x.copies-=__copies
            print("DVD lent successfully")

    def receive(self):
        __dvdno = input("Please enter CD No: ")
        __copies= input("Enter no of copies recieved: ")
        matched_data= list(x for x in self.dvdlist if x.dvdno==__dvdno)
        for x in matched_data:
            x.copies+=__copies
            print("DVD received successfully")

    def display_all(self):        
        for x in self.dvdlist:
            info(dvd=x)

    def dis_available(self):
        matched_data= list(x for x in self.dvdlist if x.copies>0)
        for x in matched_data:
            info(dvd=x)

    def dis_unavailable(self):
        matched_data= list(x for x in self.dvdlist if x.copies==0)
        for x in matched_data:
            info(dvd=x)