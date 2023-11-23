from magazineclass import magazine

def info(magazine):
    print(f"Magazine No:{magazine.mgno}, Book Title:{magazine.title}, color or black&white print{magazine.color_or_bw}, Subject:{magazine.subject}, Rental Price:{magazine.rental}, Copies Availble:{magazine.copies}")


class magazinefunction:
    def __init__(self):
        self.maglist=[]
        self.__data()

    def __data(self):
        mag1= magazine(mgno="01", title="History of Cricket color",color_or_bw="color", subject="Sports", rental=5.00, copies=5)
        mag2= magazine(mgno="02", title="Evolution of the Computer",color_or_bw="black&white", subject="Technology", rental=3.00, copies=21)
        self.maglist.append(mag1)
        self.maglist.append(mag2)
        

    def add(self):
        __mgno = input("Please enter Magazine No: ").strip().upper()
        __title= input("Enter Title: ")
        __color_or_bw= input("Enter color or black&white print: ")
        __subject= input("Enter subject: ")
        __rental=input("Enter rental per day: ")
        __copies=input("Enter no of copies: ")

        magx = magazine(mgno=__mgno, title=__title, color_or_bw=__color_or_bw, subject=__subject, rental=__rental, copies=__copies )
        self.maglist.append(magx)
        print(f"A Magazine is added successfully")

    def remove(self):
        __mgno = input("Please enter Magazine No to be removed: ")
        matched_data= list(x for x in self.maglist if x.mgno==__mgno)
        for x in matched_data:
            self.maglist.remove(x)
            print("Magazine removed successfully.")

    def lend(self):
        __mgno = input("Please enter Magazine No: ")
        __copies= input("Enter no of copies lent: ")
        matched_data= list(x for x in self.booklist if x.mgno==__mgno)
        for x in matched_data:
            x.copies-=__copies
            print("Mgazine is lent successfully")

    def receive(self):
        __mgno = input("Please enter Magazine No: ")
        __copies= input("Enter no of copies recieved: ")
        matched_data= list(x for x in self.maglist if x.mgno==__mgno)
        for x in matched_data:
            x.copies+=__copies
            print("Magazine received successfully")

    def display_all(self):        
        for x in self.maglist:
            info(magazine=x)

    def dis_available(self):
        matched_data= list(x for x in self.maglist if x.copies>0)
        for x in matched_data:
            info(magazine=x)

    def dis_unavailable(self):
        matched_data= list(x for x in self.maglist if x.copies==0)
        for x in matched_data:
            info(magazine=x)