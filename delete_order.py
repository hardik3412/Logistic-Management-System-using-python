from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector

mypass = "password_here"
mydatabase = "database_name_here"

con = mysql.connector.connect(host="localhost", user="root", password="hardik", database="lms")
cur = con.cursor()

def deleteorder():
    title = songInfo1.get()

    try:
        cur.execute("DELETE FROM orders WHERE order_id = %s", (title,))
        con.commit()
        messagebox.showinfo('Success', "Order Record Deleted Successfully")
    except:
        messagebox.showinfo("Error", "Please Check Order ID")

    songInfo1.delete(0, END)
    root.destroy()


def delete():
    global img, songInfo1, Canvas1, con, cur, root

    root = Tk()
    root.title("Delete Music Record")
    root.minsize(width=400, height=400)
    root.geometry("800x600")



    headingFrame1 = Frame(root, bg="#dfdee2", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Order", font='Helvetica 14 bold', bg="#d7a26c", fg='black',)
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg="#d7a26c")
    labelFrame.place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.2)

    lb2 = Label(labelFrame, text="order id:", font='Helvetica 11 bold', bg="#000000", fg='white')
    lb2.place(relx=0.05, rely=0.5)

    songInfo1 = Entry(labelFrame)
    songInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root, text="Submit", font='Helvetica 11 bold', bg="#d7a26c", fg='black', command=deleteorder)
    SubmitBtn.place(relx=0.28, rely=0.75, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", font='Helvetica 11 bold', bg="#d7a26c", fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.75, relwidth=0.18, relheight=0.08)

    root.mainloop()

if __name__ == "__main__":
    delete()
