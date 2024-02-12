from tkinter import *
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='log', user='root', password='hardik')
cursor = conn.cursor()

class DisplayOrders:
    def __init__(self, root):
        self.f = Frame(root.title("Display inventory"), height=500, width=900, bg='dodgerblue3')
        self.f.propagate(0)
        self.f.pack()

        self.n = Label(text='DISPLAY INVENTORY', fg="black", bg="dodgerblue3", font=('Calibri Bold', 26))
        self.n1 = Label(text='S. No.', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n2 = Label(text='NAME', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n3 = Label(text='WEIGHT', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n4 = Label(text='ADDRESS', fg="black", bg="dodgerblue3", font=('Calibri', 14))

        self.e1 = Text(self.f, height=20, width=5, fg="black", bg="white", font=('Calibri', 14))
        self.e2 = Text(self.f, height=20, width=25, fg="black", bg="white", font=('Calibri', 14))
        self.e3 = Text(self.f, height=20, width=25, fg="black", bg="white", font=('Calibri', 14))
        self.e4 = Text(self.f, height=20, width=40, fg="black", bg="white", font=('Calibri', 14))

        self.n.place(x=300, y=25)
        self.n1.place(x=50, y=100)
        self.n2.place(x=100, y=100)
        self.n3.place(x=350, y=100)
        self.n4.place(x=600, y=100)

        self.e1.place(x=50, y=125)
        self.e2.place(x=100, y=125)
        self.e3.place(x=350, y=125)
        self.e4.place(x=600, y=125)

        self.display_orders()

    def display_orders(self):
        sql = "SELECT * FROM `inventory`"
        cursor.execute(sql)
        orders = cursor.fetchall()
        i = 1
        for order in orders:
            name = order[0]
            weight = order[1]
            address = order[2]
            self.e1.insert(END, str(i) + '\n')
            self.e2.insert(END, name + '\n')
            self.e3.insert(END, str(weight) + '\n')
            self.e4.insert(END, address + '\n')
            i += 1

def display_i():
    root = Tk()
    mb = DisplayOrders(root)
    root.mainloop()

display_i()
