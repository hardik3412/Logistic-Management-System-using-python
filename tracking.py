from tkinter import *
import mysql.connector

class Tracking:
    def __init__(self, root, conn):
        self.root = root
        self.conn = conn
        self.f = Frame(root.title("Add Tracking"), height=500, width=800, bg='dodgerblue3')
        self.f.propagate(0)
        self.f.pack()

        self.n = Label(text='Tracking', fg="black", bg="dodgerblue3", font=('Calibri Bold', 26))
        self.n1 = Label(text='Date:', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n2 = Label(text='Description:', fg="black", bg="dodgerblue3", font=('Calibri', 14))
        self.n3 = Label(text='ID:', fg="black", bg="dodgerblue3", font=('Calibri', 14))

        self.b1 = Button(text='ADD Tracking', fg='white', bg='dark red', width=20, height=2,
                         command=self.buttonclick)

        self.e1 = Entry(self.f, width=25, fg="black", bg="white", font=('Calibri', 14))
        self.e2 = Entry(self.f, width=25, fg="black", bg="white", font=('Calibri', 14))
        self.e3 = Entry(self.f, width=25, fg="black", bg="white", font=('Calibri', 14))

        self.n.place(x=300, y=25)
        self.n1.place(x=50, y=100)
        self.e1.place(x=250, y=100)
        self.n2.place(x=50, y=150)
        self.e2.place(x=250, y=150)
        self.n3.place(x=50, y=200)
        self.e3.place(x=250, y=200)
        self.b1.place(x=300, y=450)

    def buttonclick(self):
        try:
            a = self.e1.get()
            b = self.e2.get()
            c = self.e3.get()
            sql_insert_tracking = "INSERT INTO tracking (id, date, description) VALUES (%s,%s,%s)"
            insert_tuple = (c, a, b)
            cursor = self.conn.cursor()
            cursor.execute(sql_insert_tracking, insert_tuple)
            self.conn.commit()
            cursor.close()
            self.root.destroy()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", "Failed to add tracking: {}".format(error))

def t_k():
    conn = mysql.connector.connect(host='localhost', database='log', user='root', password='hardik')
    root = Tk()
    mb = Tracking(root, conn)
    root.mainloop()
    conn.close()
