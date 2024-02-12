import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import mysql.connector


def validate_email(email):
    # Regular expression pattern to validate email format
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def validate_password(password):
    # Password validation criteria (example):
    # At least 8 characters long and contains at least one digit and one special character
    pattern = r'^(?=.*\d)(?=.*[@#$%^&+=]).{8,}$'
    return re.match(pattern, password)


def validate_fields():
    email_id = songInfo1.get()
    username = songInfo2.get()
    password = songInfo3.get()
    confirm_password = songInfo4.get()

    if email_id == "" or username == "" or password == "" or confirm_password == "":
        messagebox.showerror("Error", "Please fill in all the fields.")
        return False

    if not validate_email(email_id):
        messagebox.showerror("Error", "Invalid email format.")
        return False

    if len(username) < 6:
        messagebox.showerror("Error", "Username must be at least 6 characters long.")
        return False

    if not validate_password(password):
        messagebox.showerror("Error", "Invalid password format. Password must be at least 8 characters long and contain at least one digit and one special character.")
        return False

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return False

    return True


def songadd():
    if not validate_fields():
        return

    email_id = songInfo1.get()
    username = songInfo2.get()
    password = songInfo3.get()

    query = "INSERT INTO login (email_id, username, password) VALUES (%s, %s, %s)"
    values = (email_id, username, password)

    try:
        cur.execute(query, values)
        con.commit()
        messagebox.showinfo("Success", "Account added successfully.")
        root.destroy()
        import login_page
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error adding Account: {e}")


def addsong():
    global img, songInfo1, songInfo2, songInfo3, songInfo4, songInfo5, songInfo6, con, cur, root

    root = tk.Tk()
    root.title("SIGN UP PAGE")
    root.minsize(width=400, height=400)
    root.geometry("800x600")

    con = mysql.connector.connect(host="localhost", user="root", password="hardik", database="lms")
    cur = con.cursor()

    headingFrame1 = tk.Frame(root, bg="#2f2e2e", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = tk.Label(headingFrame1, text="SIGN UP PAGE", font='Helvetica 14 bold', bg="#d7a26c", fg='black')
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Frame(root, bg="#d7a26c")
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    lb1 = tk.Label(labelFrame, text="Email id:", font='Helvetica 13 bold', bg="#d7a26c", fg='black')
    lb1.place(relx=0.05, rely=0.10, relheight=0.08)

    songInfo1 = tk.Entry(labelFrame)
    songInfo1.place(relx=0.3, rely=0.10, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame, text="Username:", font='Helvetica 13 bold', bg="#d7a26c", fg='black')
    lb2.place(relx=0.05, rely=0.26, relheight=0.08)

    songInfo2 = Entry(labelFrame)
    songInfo2.place(relx=0.3, rely=0.26, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame, text="Password:", font='Helvetica 13 bold', bg="#d7a26c", fg='black')
    lb3.place(relx=0.05, rely=0.42, relheight=0.08)

    songInfo3 = Entry(labelFrame, show="*")  # Use show="*" to hide password input
    songInfo3.place(relx=0.3, rely=0.42, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame, text="Confirm Password:", font='Helvetica 13 bold', bg="#d7a26c", fg='black')
    lb4.place(relx=0.05, rely=0.58, relheight=0.08)

    songInfo4 = Entry(labelFrame, show="*")  # Use show="*" to hide password input
    songInfo4.place(relx=0.3, rely=0.58, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root, text="Submit", font='Helvetica 12 bold', bg='#d7a26c', fg='black', command=songadd)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", font='Helvetica 12 bold', bg='#d7a26c', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


addsong()



