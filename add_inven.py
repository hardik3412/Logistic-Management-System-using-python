
from tkinter import *
from LogMSys import *
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='log', user='root', password='hardik')
cursor = conn.cursor()


class add_book:
    def __init__(self, root):
        self.root = root
        self.f = Frame(root.title("Add Order"), height=500, width=800, bg='dodgerblue3')
        self.f.propagate(0)
        self.f.pack()

        self.n = Label(text='inventory DETAILS', fg="black", bg="dodgerblue3", font=('Calibri Bold', 26))
        self.n1 = Label(text='NAME:', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n2 = Label(text='WEIGHT:', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n3 = Label(text='ADDRESS:', fg="black", bg="dodgerblue3", font=('Calibri', 14))

        self.b1 = Button(text='ADD', fg='white', bg='dark red', width=20, height=2,
                         command=lambda: self.buttonclick(0))

        self.e1 = Entry(self.f, width=25, fg="black", bg="white", font=('Calibri', 14))
        self.e2 = Entry(self.f, width=25, fg="black", bg="white", font=('Calibri', 14))
        self.e3 = Entry(self.f, width=25, fg="black", bg="white", font=('Calibri', 14))
        self.e4 = Entry(self.f, width=25, fg="black", bg="white", font=('Calibri', 14))

        self.n.place(x=300, y=25)
        self.n1.place(x=50, y=100)
        self.e1.place(x=250, y=100)
        self.n2.place(x=50, y=150)
        self.e2.place(x=250, y=150)
        self.n3.place(x=50, y=200)
        self.e3.place(x=250, y=200)
        #self.e4.place(x=250, y=250)
        self.b1.place(x=300, y=450)

    def buttonclick(self, num):
        a = self.e1.get()
        b = self.e2.get()
        c = self.e3.get()
        #d = self.e4.get()
        if num == 0:
            sql_insert_book = "INSERT INTO inventory (name, weight, address) VALUES (%s,%s,%s)"
            insert_tuple_1 = (a, b, c)
            cursor.execute(sql_insert_book, insert_tuple_1)
            self.root.destroy()
            mp()
            conn.commit()
            cursor.close()
            conn.close()

        else:
            return


def ad_i():
    root = Tk()
    mb = add_book(root)
    root.mainloop()