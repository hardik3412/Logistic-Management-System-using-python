import tkinter as tk
import mysql.connector
from tkinter import ttk


con = mysql.connector.connect(host="localhost", user="root", password="hardik", database="lms")
cur = con.cursor()


def view_all_songs():
    root = tk.Tk()
    root.title("View All Inventory")
    root.minsize(width=400, height=400)
    root.geometry("1000x400")

    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Product id")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Product Name")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Stock Level")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Incoming Stock")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Outgoing Stock")
    tree.column("#6", anchor=tk.CENTER)
    tree.heading("#6", text="Cost:")
    tree.pack(expand=True, fill=tk.BOTH)

    try:
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        con.commit()
        for i in rows:
            tree.insert("", tk.END, values=i)
    except:
        tk.messagebox.showinfo("Error", "Failed to fetch orders from the database")

    quit_btn = tk.Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_btn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

if __name__ == "__main__":
    view_all_songs()
