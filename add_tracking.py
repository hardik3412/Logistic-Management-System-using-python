from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

# Insert function
def insert():
    shipment_id = e_id.get()
    order_id = e_name.get()
    tracking_number = e_phone.get()
    current_location = e_bill.get()
    date = e_date.get()

    if shipment_id == "" or order_id == "" or tracking_number == "" or current_location == "":
        MessageBox.showinfo("Insert Status", "All Fields are Required!")
    else:
        con = mysql.connect(host="localhost", user="root", password="hardik", database="lms")
        cursor = con.cursor()
        query = "INSERT INTO shipments (shipment_id, order_id, tracking_number, current_location, date) VALUES (%s, %s, %s, %s, %s)"
        values = (shipment_id, order_id, tracking_number, current_location, date)
        cursor.execute(query, values)
        con.commit()
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_bill.delete(0, 'end')
        show()
        MessageBox.showinfo("Insert Status", "Inserted Successfully!")
        con.close()
def mainpage():
    #import Mainpage
    os.system('python Mainpage.py')

# Delete function
def delete():
    if e_id.get() == "":
        MessageBox.showinfo("Delete Status", "You need to specify ID!")
    else:
        con = mysql.connect(host="localhost", user="root", password="hardik", database="lms")
        cursor = con.cursor()
        cursor.execute("DELETE FROM shipments WHERE shipment_id = %s", (e_id.get(),))
        cursor.execute("commit")
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_bill.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete Status", "Deleted Successfully!")
        con.close()

# Update function
def update():
    shipment_id = e_id.get()
    order_id = e_name.get()
    tracking_number = e_phone.get()
    current_location = e_bill.get()
    date = e_date.get()

    if shipment_id == "" or order_id == "" or tracking_number == "" or current_location == "":
        MessageBox.showinfo("Update Status", "All Fields are Required!")
    else:
        con = mysql.connect(host="localhost", user="root", password="hardik", database="lms")
        cursor = con.cursor()
        cursor.execute(
            "UPDATE shipments SET order_id = %s, tracking_number = %s, current_location = %s, date = %s WHERE shipment_id = %s",
            (order_id, tracking_number, current_location, date, shipment_id))
        cursor.execute("commit")
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_bill.delete(0, 'end')
        show()
        MessageBox.showinfo("Update Status", "Updated Successfully!")
        con.close()

# Get function
def get():
    shipment_id = e_id.get()
    if e_id.get() == "":
        MessageBox.showinfo("Fetch Status", "You need to specify ID!")
    else:
        con = mysql.connect(host="localhost", user="root", password="hardik", database="lms")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM shipments WHERE shipment_id = %s", (e_id.get(),))

        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])
            e_bill.insert(0, row[3])

        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", password="hardik", database="lms")
    cursor = con.cursor()
    cursor.execute("select * from shipments ")
    rows = cursor.fetchall()

    # clear the existing data in the list widget
    list.delete(0, list.size())

    # Clear the existing data in the list widget
    list.delete(0, END)



    # Insert data into the list widget
    for row in rows:
        insertData = str(row[0]) + '      ' + str(row[1]) + '      ' + row[2] + '     ' + str(row[3]) + '      '
        list.insert(END, insertData)

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

id = Label(root, text='Enter Shipment ID', font=('bold', 14))
id.place(x=400, y=200)

name = Label(root, text='Enter Order ID', font=('bold',14))
name.place(x=400, y=230)

phone = Label(root, text='Enter Location', font=('bold', 14))
phone.place(x=400, y=290)

bill = Label(root, text='Enter Tracking No', font=('bold', 14))
bill.place(x=400, y=260)

date = Label(root, text='Enter Date', font=('bold', 14))
date.place(x=400, y=320)

e_date = Entry()
e_date.place(x=610, y=320)

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