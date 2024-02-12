import tkinter as tk
import mysql.connector
from tkinter import ttk
from tkinter import messagebox

con = mysql.connector.connect(host="localhost", user="root", password="hardik", database="lms")
cur = con.cursor()
search_entry = None
search_option = None
start_date_entry = None
end_date_entry = None
tree=None


def search_data():
    global search_entry, search_option, start_date_entry, end_date_entry,tree
    keyword = search_entry.get()
    search_by = search_option.get()

    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    if search_by == "Order ID":
        query = """SELECT orders.order_id, orders.order_date, shipments.tracking_number, shipments.current_location, shipments.shipment_id, orders.description
                   FROM orders
                   INNER JOIN shipments ON orders.order_id = shipments.order_id
                   WHERE orders.order_id = %s;
                """
    elif search_by == "Shipment ID":
        query = """SELECT orders.order_id, orders.order_date, shipments.tracking_number, shipments.current_location, shipments.shipment_id, orders.description
                   FROM orders
                   INNER JOIN shipments ON orders.order_id = shipments.order_id
                   WHERE shipments.shipment_id = %s;
                """
    elif search_by == "Date Range":
        query = """SELECT orders.order_id, orders.order_date, shipments.tracking_number, shipments.current_location, shipments.shipment_id, orders.description
                   FROM orders
                   INNER JOIN shipments ON orders.order_id = shipments.order_id
                   WHERE orders.order_date BETWEEN %s AND %s;
                """
    else:
        messagebox.showinfo("Error", "Invalid search option selected")
        return

    try:
        if search_by == "Date Range":
            cur.execute(query, (start_date, end_date))
        else:
            cur.execute(query, (keyword,))

        rows = cur.fetchall()
        con.commit()

        tree.delete(*tree.get_children())

        for i in rows:
            tree.insert("", tk.END, values=i)

    except Exception as e:
        messagebox.showinfo("Error", f"Failed to fetch data from the database: {str(e)}")


def view_all_songs():
    global search_entry, search_option, start_date_entry, end_date_entry,tree
    root = tk.Tk()
    root.title("View All Tracking")
    root.minsize(width=400, height=400)
    root.geometry("1000x400")

    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)

    search_label = tk.Label(search_frame, text="Search By:")
    search_label.grid(row=0, column=0, padx=5)

    search_option = ttk.Combobox(search_frame, values=["Order ID", "Shipment ID", "Date Range"])
    search_option.grid(row=0, column=1, padx=5)

    search_entry = tk.Entry(search_frame)
    search_entry.grid(row=0, column=2, padx=5)

    start_date_label = tk.Label(search_frame, text="Start Date:")
    start_date_label.grid(row=0, column=3, padx=5)

    start_date_entry = tk.Entry(search_frame)
    start_date_entry.grid(row=0, column=4, padx=5)

    end_date_label = tk.Label(search_frame, text="End Date:")
    end_date_label.grid(row=0, column=5, padx=5)

    end_date_entry = tk.Entry(search_frame)
    end_date_entry.grid(row=0, column=6, padx=5)

    search_button = tk.Button(search_frame, text="Search", command=search_data)
    search_button.grid(row=0, column=7, padx=5)

    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Order id")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Date")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Tracking Number")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Current Location")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Shipment ID")
    tree.column("#6", anchor=tk.CENTER)
    tree.heading("#6", text="Description:")
    tree.pack(expand=True, fill=tk.BOTH)

    try:
        cur.execute("""SELECT orders.order_id, orders.order_date, shipments.tracking_number, shipments.current_location, shipments.shipment_id, orders.description
                           FROM orders
                           INNER JOIN shipments ON orders.order_id = shipments.order_id;
            """)

        rows = cur.fetchall()
        con.commit()

        for i in rows:
            tree.insert("", tk.END, values=i)
    except Exception as e:
        messagebox.showinfo("Error", f"Failed to fetch orders from the database: {str(e)}")

    quit_btn = tk.Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_btn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


if __name__ == "__main__":
    view_all_songs()



