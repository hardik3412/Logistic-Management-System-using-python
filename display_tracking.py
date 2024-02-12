from tkinter import *
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='log', user='root', password='hardik')
cursor = conn.cursor()

class Display:
    def __init__(self, root):
        self.root = root
        self.f = Frame(root.title("Display Tracking"), height=500, width=800, bg='dodgerblue3')
        self.f.propagate(0)
        self.f.pack()

        self.n = Label(text='Display Tracking', fg="black", bg="dodgerblue3", font=('Calibri Bold', 26))
        self.n1 = Label(text='ID', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n2 = Label(text='Date', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n3 = Label(text='Description', fg="black", bg="dodgerblue3", font=('Calibri', 14))

        self.n.place(x=300, y=25)
        self.n1.place(x=50, y=100)
        self.n2.place(x=50, y=150)
        self.n3.place(x=50, y=200)

        # create table to display details
        self.tree = ttk.Treeview(self.f, columns=('id', 'date', 'description'), height=10, show='headings')
        self.tree.place(x=200, y=100)

        # set column headings
        self.tree.heading('id', text='ID')
        self.tree.heading('date', text='Date')
        self.tree.heading('description', text='Description')

        # fetch data from database and display in table
        cursor.execute('SELECT * FROM tracking')
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", END, values=row)

def d_k():
    root = Tk()
    mb = Display(root)
    root.mainloop()

# call the display function to show the details
d_k()
