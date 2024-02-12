import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

def update_inventory():
    product_id = songInfo1.get()
    stock_level = songInfo2.get()
    incoming_stock = songInfo3.get()
    outgoing_stock = songInfo4.get()
    cost = songInfo5.get()

    if product_id == "" or stock_level == "" or incoming_stock == "" or outgoing_stock == "" or cost == "":
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    query = "UPDATE products SET stock_level = %s, incoming_stock = %s, outgoing_stock = %s, cost = %s WHERE product_id = %s"
    values = (stock_level, incoming_stock, outgoing_stock, cost, product_id)

    try:
        cur.execute(query, values)
        con.commit()
        messagebox.showinfo("Success", "Inventory updated successfully.")
        root.destroy()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error updating inventory: {e}")

def validate_stock(event):
    if not songInfo2.get().isdigit():
        songInfo2.delete(0, END)
        messagebox.showerror("Error", "Stock Level must be a number.")

def validate_incoming_stock(event):
    if not songInfo3.get().isdigit():
        songInfo3.delete(0, END)
        messagebox.showerror("Error", "Value must be a number.")

def validate_outgoing_stock(event):
    if not songInfo4.get().isdigit():
        songInfo4.delete(0, END)
        messagebox.showerror("Error", "Value must be a number.")

def validate_cost(event):
    if not songInfo5.get().isdigit():
        songInfo5.delete(0, END)
        messagebox.showerror("Error", "Cost must be a number.")

def updateinven():
    global songInfo1, songInfo2, songInfo3, songInfo4, songInfo5, con, cur, root

    root = tk.Tk()
    root.title("Update Inventory")
    root.minsize(width=400, height=400)
    root.geometry("800x600")

    con = mysql.connector.connect(host="localhost", user="root", password="hardik", database="lms")
    cur = con.cursor()

    headingFrame1 = tk.Frame(root, bg="#2f2e2e", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = tk.Label(headingFrame1, text="Update Inventory", font='Helvetica 14 bold', bg="#d7a26c", fg='black')
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Frame(root, bg="#d7a26c")
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    lb1 = tk.Label(labelFrame, text="Product ID:", font='Helvetica 13 bold', bg="#d7a26c", fg='black')
    lb1.place(relx=0.05, rely=0.10, relheight=0.08)

    songInfo1 = tk.Entry(labelFrame)
    songInfo1.place(relx=0.3, rely=0.10, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame, text="Stock Level:", font='Helvetica 13 bold', bg="#d7a26c", fg='black')
    lb2.place(relx=0.05, rely=0.26, relheight=0.08)

    songInfo2 = Entry(labelFrame)
    songInfo2.place(relx=0.3, rely=0.26, relwidth=0.62, relheight=0.08)
    songInfo2.bind("<KeyRelease>", validate_stock)

    lb3 = Label(labelFrame, text="Incoming Stock:", font='Helvetica 13 bold', bg="#d7a26c", fg='black')
    lb3.place(relx=0.05, rely=0.42, relheight=0.08)

    songInfo3 = Entry(labelFrame)
    songInfo3.place(relx=0.3, rely=0.42, relwidth=0.62, relheight=0.08)
    songInfo3.bind("<KeyRelease>", validate_incoming_stock)

    lb4 = Label(labelFrame, text="Outgoing Stock:", font='Helvetica 13 bold', bg="#d7a26c", fg='black')
    lb4.place(relx=0.05, rely=0.58, relheight=0.08)

    songInfo4 = Entry(labelFrame)
    songInfo4.place(relx=0.3, rely=0.58, relwidth=0.62, relheight=0.08)
    songInfo4.bind("<KeyRelease>", validate_outgoing_stock)

    lb5 = Label(labelFrame, text="Cost:", font='Helvetica 13 bold', bg="#d7a26c", fg='black')
    lb5.place(relx=0.05, rely=0.74, relheight=0.08)

    songInfo5 = Entry(labelFrame)
    songInfo5.place(relx=0.3, rely=0.74, relwidth=0.62, relheight=0.08)
    songInfo5.bind("<KeyRelease>", validate_cost)

    submitBtn = Button(root, text="Update", font='Helvetica 12 bold', bg='#d7a26c', fg='black',
                       command=update_inventory)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", font='Helvetica 12 bold', bg='#d7a26c', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


updateinven()





