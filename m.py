from tkinter import *
from add_user import *
from add_order import *
from delete_order import *
from LogMSys import *
from inventory import *


class main_page:
    def __init__(self, root):
        self.root = root
        self.f = Frame(root.title("Main Page"), height=500, width=800, bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()

        #####
        # Heading
        self.n1 = Label(text='Welcome to Logistics Management System', bg='dodgerblue3', font=('Arial Bold', 25))
        self.n1.place(x=110, y=20)

        self.b_addBook = Button(text='Order Management', fg='white', bg="dark red", width=25, height=1, font=('Calibri', 14),
                                command=lambda: self.buttonclick(1))
        self.b_addBook.place(x=250, y=150)

        self.b_deleteBook = Button(text='Shipping Management ', fg='white', bg="dark red", width=25, height=1,
                                   font=('Calibri', 14), command=lambda: self.buttonclick(2))
        self.b_deleteBook.place(x=250, y=200)
        #####


        self.b_returnBook = Button(text='Inventory Management', fg='white', bg="dark red", width=25, height=1,
                                   font=('Calibri', 14), command=lambda: self.buttonclick(0))
        self.b_returnBook.place(x=250, y=250)

    def buttonclick(self, num):
        if (num == 0):
            self.root.destroy()
            inventory()
            cursor.close()
            conn.close()
        elif (num == 1):
            self.root.destroy()
            mp()
            cursor.close()
            conn.close()
        elif (num == 2):
            self.root.destroy()
            dele()
            cursor.close()
            conn.close()
        else:
            self.root.destroy()


def m():
    root = Tk()

    mb = main_page(root)

    root.mainloop()
