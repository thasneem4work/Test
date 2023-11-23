from cdclass import cd

def info(cd):
    print(f"CD No:{cd.cdno}, CD Title:{cd.title}, Subject:{cd.subject}, Rental Price:{cd.rental}, Copies Availble:{cd.copies}")


class cdfunction:
    def __init__(self):
        self.cdlist=[]
        self.__data()

    def __data(self):
        cd1= cd(cdno=21, title="Basic of western music",subject="Music", rental=1.50, copies=11)
        cd2= cd(cdno=22, title="Japanese Language",subject="Foriegn Language", rental=2.00, copies=3)
        
        self.cdlist.append(cd1)
        self.cdlist.append(cd2)

    def add(self):
        __cdno = input("Please enter CD No: ").strip().upper()
        __title= input("Enter Title: ")
        __subject= input("Enter subject: ")
        __rental=input("Enter rental per day: ")
        __copies=input("Enter no of copies: ")

        cdx = cd(cdno=__cdno, title=__title, subject=__subject, rental=__rental, copies=__copies )
        self.cdlist.append(cdx)
        print(f"A book is added successfully")

    def remove(self):
        __cdno = input("Please enter CD No to be removed: ")
        matched_data= list(x for x in self.cdlist if x.cdno==__cdno)
        for x in matched_data:
            self.cdlist.remove(x)
            print("CD removed successfully.")

    def lend(self):
        __cdno = input("Please enter CD No: ")
        __copies= input("Enter no of copies lent: ")
        matched_data= list(x for x in self.cdlist if x.cdno==__cdno)
        for x in matched_data:
            x.copies-=__copies
            print("CD lent successfully")

    def receive(self):
        __cdno = input("Please enter CD No: ")
        __copies= input("Enter no of copies recieved: ")
        matched_data= list(x for x in self.cdlist if x.cdno==__cdno)
        for x in matched_data:
            x.copies+=__copies
            print("CD received successfully")

    def display_all(self):        
        for x in self.cdlist:
            info(cd=x)

    def dis_available(self):
        matched_data= list(x for x in self.cdlist if x.copies>0)
        for x in matched_data:
            info(cd=x)

    def dis_unavailable(self):
        matched_data= list(x for x in self.cdlist if x.copies==0)
        for x in matched_data:
            info(cd=x)
