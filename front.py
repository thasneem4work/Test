from bookfunction import Bookfunction
from magazinefunction import magazinefunction
from cdfunction import cdfunction
from dvdfunction import dvdfunction

book_function= Bookfunction()
mag_function= magazinefunction()
dvd_function = dvdfunction()
cd_function= cdfunction()

def menu():
    print("Resources Available\n")

    print("1 - Book")
    print("2 - Magazine")
    print("3 - Educational DVD")
    print("4 - Lecture CD")
    print("5 - Search by subject")
    print("6 - Stop\n")

def secondmenu(function):
    b=1
    while b>0:
        print("Please select from below\n")
        print("1 - Add")
        print("2 - remove")
        print("3 - Display available")
        print("4 - Display unavailable")
        print("5 - Display all")
        print("6 - Recieve")
        print("7 - lend")
        print("8 - Back to main menu")
        print("9 - Quit\n")

        b= int(input("Type your choice: "))
        print("\n")
        if b==1:
            function.add()

        elif b==2:
            function.remove()

        elif b==3:
            function.dis_available()

        elif b==4:
            function.dis_unavailable()

        elif b==5:
            function.display_all()

        elif b==6:
            function.receive()  

        elif b==7:
            function.lend()

        elif b==8:
            menu()

        elif b==9:
            print("THANK YOU! Have a nice day!")
            quit()

        else:
            print("choice not valid")
        print("\n")
    
    

print(" Welcome to the university library system !!!")
print("*********************************************\n")

a=1
while a>0:
    menu()
    try:
        a = int(input("Type your choice: "))
        print("\n")

    except ValueError:
        print("wrong input")    
        menu()

    if a==1:
        function= book_function
        secondmenu(function)
        break

    elif a==2:
        function= mag_function
        secondmenu(function)
        break

    elif a==3:
        function= dvd_function
        secondmenu(function)
        break

    elif a==4:
        function= cd_function
        secondmenu(function)
        break
    
    elif a==6:
        print("THANK YOU! Have a nice day!")
        quit()

