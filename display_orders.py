import os
from tkinter import *
from LogMSys import *
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='log', user='root', password='hardik')
cursor = conn.cursor()


class DisplayOrders:
    def __init__(self, root):
        self.root = root
        self.f = Frame(root.title("Display Orders"), height=500, width=900, bg='dodgerblue3')
        self.f.propagate(0)
        self.f.pack()


        self.n = Label(text='DISPLAY ORDERS', fg="black", bg="dodgerblue3", font=('Calibri Bold', 26))
        self.n1 = Label(text='S. No.', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n2 = Label(text='ID', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n3 = Label(text='ORDER WEIGHT', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n4 = Label(text='ORDER ADDRESS', fg="black", bg="dodgerblue3", font=('Calibri', 14))

        self.e1 = Text(self.f, height=20, width=5, fg="black", bg="white", font=('Calibri', 14))
        self.e2 = Text(self.f, height=20, width=25, fg="black", bg="white", font=('Calibri', 14))
        self.e3 = Text(self.f, height=20, width=25, fg="black", bg="white", font=('Calibri', 14))
        self.e4 = Text(self.f, height=20, width=40, fg="black", bg="white", font=('Calibri', 14))
        self.b_addBook = Button(text='MENU', fg='white', bg='dark red', width=20, height=2,command=lambda: self.buttonclick(0))

        self.n.place(x=300, y=25)
        self.n1.place(x=50, y=100)
        self.n2.place(x=100, y=100)
        self.n3.place(x=350, y=100)
        self.n4.place(x=600, y=100)

        self.e1.place(x=50, y=125)
        self.e2.place(x=100, y=125)
        self.e3.place(x=350, y=125)
        self.e4.place(x=600, y=125)
        self.b_addBook.place(x=300, y=450)

        self.display_orders()
    def buttonclick(self,num):
        if(num==0):
            self.root.destroy()
            mp()
            cursor.close()
            conn.close()

    def display_orders(self):
        sql = "SELECT id, weight, address FROM orders"
        cursor.execute(sql)
        orders = cursor.fetchall()
        i = 1
        for order in orders:
            id = order[0]
            weight = order[1]
            address = order[2]
            self.e1.insert(END, str(i) + '\n')
            self.e2.insert(END, str(id) + '\n')
            self.e3.insert(END, str(weight) + '\n')
            self.e4.insert(END, address + '\n')
            i += 1

def display_orders():
    root = Tk()
    mb = DisplayOrders(root)
    root.mainloop()

display_orders()
