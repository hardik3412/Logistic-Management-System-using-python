from tkinter import *
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='log', user='root', password='hardik')
cursor = conn.cursor()


class add_book:
    def __init__(self, root):
        self.f = Frame(root.title("Delete Order"), height=500, width=800, bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()

        self.n = Label(text='DELETE ORDER', fg="black", bg="dodgerblue3", font=('Calibri Bold', 26))
        self.n1 = Label(text='NAME:', fg="black", bg="dodgerblue3", font=('Calibri', 14))

        self.b1 = Button(text='DELETE Order', fg='white', bg='dark red', width=20, height=2,
                         command=lambda: self.buttonclick())

        self.e1 = Entry(self.f, width=25, fg="black", bg="white", font=('Calibri', 14))

        self.n.place(x=300, y=25)
        self.n1.place(x=50, y=100)
        self.e1.place(x=250, y=100)

        self.b1.place(x=300, y=350)

    def buttonclick(self):
        name = self.e1.get()

        sql_delete_order = "DELETE FROM orders WHERE id = %s"
        cursor.execute(sql_delete_order, (name,))
        conn.commit()

        cursor.close()
        conn.close()

    def quit(self):
        self.f.quit()


def dele():
    root = Tk()

    mb = add_book(root)

    root.mainloop()
