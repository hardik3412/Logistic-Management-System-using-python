
from tkinter import *
from LogMSys import *
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='log', user='root', password='hardik')
cursor = conn.cursor()


class add_book:
    def __init__(self, root):
        self.root = root
        self.f = Frame(root.title("Add Order"), height=500, width=800, bg='dodgerblue3')
        self.f.propagate(0)
        self.f.pack()

        self.n = Label(text='ORDER DETAILS', fg="black", bg="dodgerblue3", font=('Calibri Bold', 26))
        self.n1 = Label(text='ID:', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n2 = Label(text='ORDER WEIGHT:', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n3 = Label(text='ORDER ADDRESS:', fg="black", bg="dodgerblue3", font=('Calibri', 14))

        self.b1 = Button(text='ADD ORDER', fg='white', bg='dark red', width=20, height=2,
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
        if not b.isdigit():
            messagebox.showerror("Error", "ID must be a number.")
        if not a.isdigit():
            messagebox.showerror("Error", "ID must be a number.")
        if num == 0:
            sql_insert_book = "INSERT INTO orders (id, weight, address) VALUES (%s,%s,%s)"
            insert_tuple_1 = (a, b, c)
            cursor.execute(sql_insert_book, insert_tuple_1)
            #mp()
            self.root.destroy()
            conn.commit()
            cursor.close()
            conn.close()

        else:
            return

    def validate_id(self, id):
        if not id:
            messagebox.showerror("Error", "ID cannot be empty.")
            return False
        elif not id.isdigit():
            messagebox.showerror("Error", "ID must be a number.")
            return False
        else:
            # check if the id already exists in the database
            sql_select_book = "SELECT * FROM orders WHERE id = %s"
            cursor.execute(sql_select_book, (id,))
            result = cursor.fetchone()
            if result:
                messagebox.showerror("Error", "ID already exists.")
                return False
            else:
                return True


def ad_bk():
    root = Tk()
    mb = add_book(root)
    root.mainloop()
