from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk
import os

def insert():
    id = e_id.get();
    name = e_name.get();
    phone = e_phone.get();
    bill = e_bill.get();

    if (id == "" or name == "" or phone == "" or bill == ""):
        MessageBox.showinfo("Insert Status", "All Fields are Required!")
    else:
        con = mysql.connect(host="localhost", user="root", password="hardik", database="lms")
        cursor = con.cursor()
        cursor.execute("insert into customer values('" + id + "','" + name + "','" + phone + "','" + bill + "')")
        cursor.execute("commit");
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_bill.delete(0, 'end')
        show()
        MessageBox.showinfo("Insert Status", "Inserted Successfully!")
        con.close();

def mainpage():
    #import Mainpage
    os.system('python Mainpage.py')

def delete():
    if (e_id.get() == ""):
        MessageBox.showinfo("Delete Status", "You need to specify ID!")
    else:
        con = mysql.connect(host="localhost", user="root", password="hardik", database="lms")
        cursor = con.cursor()
        cursor.execute("delete from customer where id='" + e_id.get() + "'")
        cursor.execute("commit");
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_bill.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete Status", "Deleted Successfully!")
        con.close();


def update():
    id = e_id.get();
    name = e_name.get();
    phone = e_phone.get();
    bill = e_bill.get();

    if (id == "" or name == "" or phone == "" or bill == ""):
        MessageBox.showinfo("Update Status", "All Fields are Required!")
    else:
        con = mysql.connect(host="localhost", user="root", password="hardik", database="lms")
        cursor = con.cursor()
        cursor.execute(
            "update customer set name='" + name + "', phone='" + phone + "', bill='" + bill + "' where id='" + id + "'")
        cursor.execute("commit");
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_bill.delete(0, 'end')
        show()
        MessageBox.showinfo("Update Status", "Updated Successfully!")
        con.close();


def get():
    if (e_id.get() == ""):
        MessageBox.showinfo("Fetch Status", "You need to specify ID!")
    else:
        con = mysql.connect(host="localhost", user="root", password="hardik", database="lms")
        cursor = con.cursor()
        cursor.execute("select * from customer where id='" + e_id.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])
            e_bill.insert(0, row[3])

        con.close();


def show():
    con = mysql.connect(host="localhost", user="root", password="hardik", database="lms")
    cursor = con.cursor()
    cursor.execute("select * from customer")
    rows = cursor.fetchall()

    # clear the existing data in the list widget
    list.delete(0, list.size())

    # create labels for column names
    id_label = Label(root, text="ID", font=("Helvetica", 10, "bold"))
    id_label.grid(row=1, column=0, padx=5, pady=5)
    name_label = Label(root, text="Name", font=("Helvetica", 10, "bold"))
    name_label.grid(row=1, column=1, padx=5, pady=5)
    phone_label = Label(root, text="Phone", font=("Helvetica", 10, "bold"))
    phone_label.grid(row=1, column=2, padx=5, pady=5)
    bill_label = Label(root, text="Bill", font=("Helvetica", 10, "bold"))
    bill_label.grid(row=1, column=3, padx=5, pady=5)

    # insert data into the list widget
    for row in rows:
        insertData = str(row[0]) + '      ' + row[1] + '      ' + str(row[2]) + '     ' + str(row[3]) + '      '
        list.insert(list.size() + 1, insertData)

    con.close()


root = Tk()
root.geometry('1200x1800')
root.title('Customer Records')
header = Label(root, text="Logostic Management System", font=("Helvetica", 24, "bold"), bg="brown", fg="white")
header.place(x=0, y=0, width=1200, height=50)

header = Label(root, text="Add Order", font=("Helvetica", 24, "bold"), bg="brown", fg="white")
header.place(x=0, y=100, width=1200, height=50)



#header2 = Label(root, text="ADD ORDER", font=("Helvetica", 20, "bold"))
#header2.place(x=50, y=100)

# Load the background image
#bg_image = Image.open("103.jpeg")
#bg_image = bg_image.resize((1200, 1800), Image.ANTIALIAS)
#background_image = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
#background_label = Label(root, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

id = Label(root, text='Enter ID', font=('bold', 14))
id.place(x=400, y=200)

name = Label(root, text='Enter Name', font=('bold',14))
name.place(x=400, y=230)

phone = Label(root, text='Enter Phone', font=('bold', 14))
phone.place(x=400, y=260)

bill = Label(root, text='Enter Pending Bills', font=('bold', 14))
bill.place(x=400, y=290)

e_id = Entry()
e_id.place(x=610, y=200)

e_name = Entry()
e_name.place(x=610, y=230)

e_phone = Entry()
e_phone.place(x=610, y=260)

e_bill = Entry()
e_bill.place(x=610, y=290)

insert = Button(root, text="Insert", font=("italic", 15), bg="brown", fg="white", command=insert)
insert.place(x=400, y=340)


delete = Button(root, text="Delete", font=("italic", 15), bg="brown",fg="white", command=delete)
delete.place(x=490, y=340)

update = Button(root, text="Update", font=("italic", 15), bg="brown",fg="white", command=update)
update.place(x=580, y=340)

get = Button(root, text="Get", font=("italic", 15), bg="brown",fg="white", command=get)
get.place(x=670, y=340)

insert = Button(root, text="Menu", font=("italic", 15), bg="brown",fg="white", command=mainpage)
insert.place(x=400, y=500)

list = Listbox(root)
list.place(x=780, y=200)
show()
mainloop()