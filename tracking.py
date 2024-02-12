import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

root = Tk()
root.title("Search Shipment")
root.geometry("900x500+200+100")
root.resizable(False, False)
global root_window
root_window = root

def on_closing():
    root_window.destroy()

def search():
    option = dropdown.get()
    search_input = searchInput.get()
    db = mysql.connector.connect(host="localhost", user="root", password="hardik", database="lms")
    mycursor = db.cursor(buffered=True)
    if option == "Tracking Number":
        mycursor.execute("SELECT * FROM shipments WHERE tracking_number = '" + str(search_input) + "'")
    elif option == "Shipment ID":
        mycursor.execute("SELECT * FROM shipments WHERE shipment_id = '" + str(search_input) + "'")
    else:
        return
    rows = mycursor.fetchone()
    if rows is None:
        draw_no_result()
        return
    draw_result()
    global result, result_shipment_id, result_order_id, result_tracking_number, result_location
    result_shipment_id["text"] = rows[0]
    result_order_id["text"] = rows[1]
    result_tracking_number["text"] = rows[2]
    result_location["text"] = rows[3]
    db.commit()
    db.close()

def draw_result():
    global result, result_shipment_id, result_order_id, result_tracking_number, result_location
    for widget in result.winfo_children():
        widget.destroy()
    result = Frame(root, bg="#777", bd=0)
    result.place(x=100, y=200, width=700, height=250)
    shipment_id = Label(result, text="Shipment ID:", font=("Minion Pro Regular", 20), bd=0, bg="#777", fg="#fff")
    shipment_id.place(x=100, y=60, height=30)
    result_shipment_id = Label(result, text="", font=("Minion Pro Regular", 20), bd=0, bg="#777", fg="#fff")
    result_shipment_id.place(x=350, y=60, height=30)
    order_id = Label(result, text="Order ID:", font=("Minion Pro Regular", 20), bd=0, bg="#777", fg="#fff")
    order_id.place(x=100, y=90, height=30)
    result_order_id = Label(result, text="", font=("Minion Pro Regular", 20), bd=0, bg="#777", fg="#fff")
    result_order_id.place(x=350, y=90, height=30)
    tracking_number = Label(result, text="Tracking Number:", font=("Minion Pro Regular", 20), bd=0, bg="#777", fg="#fff")
    tracking_number.place(x=100, y=120, height=30)
    result_tracking_number = Label(result, text="", font=("Minion Pro Regular", 20), bd=0, bg="#777", fg="#fff")
    result_tracking_number.place(x=350, y=120, height=30)
    location = Label(result, text="Current Location:", font=("Minion Pro Regular", 20), bd=0, bg="#777", fg="#fff")
    location.place(x=100, y=150, height=30)
    result_location = Label(result, text="", font=("Minion Pro Regular", 20), bd=0, bg="#777", fg="#fff")
    result_location.place(x=350, y=150, height=30)

def draw_no_result():
    global result
    for widget in result.winfo_children():
        widget.destroy()
    result = Frame(root, bg="#777", bd=0)
    result.place(x=100, y=200, width=700, height=250)
    no_record_label = Label(result, text="No record found", font=("Minion Pro Regular", 20), bd=0, bg="#777", fg="#fff")
    no_record_label.place(x=0, y=100, height=30, width=700)

header = Frame(root, bg="brown", bd=0)
header.place(x=0, y=0, width=900, height=75)

nsec = Label(header, text="Logistic Management system", font=("Helvetica", 28, "bold"), bg="brown", fg="#eae2b7")
nsec.place(x=0, y=10, width=900)

frame2 = Frame(root, bg="#fbb1bd")
frame2.place(x=0, y=75, width=900, height=50)
welcome_text = Label(frame2, text="Search Shipments (by Tracking Number OR Shipment ID)",
font=("Minion Pro Regular", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)

close = Button(frame2, text="Close", bd=0, command=on_closing, font=("Minion Pro Regular", 16), bg="#fff", fg="#000")
close.place(x=830, y=0, height=50, width=70)


panel = Frame(root, bg="#bbb", bd=0)
panel.place(x=0, y=125, width=900, height=375)

searchBy = Label(panel, text="Enter Value", font=("Minion Pro Regular", 16), bg="#bbb", fg="#222")
searchBy.place(x=100, y=20)
searchInput = Entry(panel, font=("Minion Pro Regular", 12), bd=0)
searchInput.place(x=230, y=20, height=30, width=220)
dropdown = ttk.Combobox(panel, width=15, font=("Minion Pro Regular", 16), state='readonly')
dropdown['values'] = ("--search by--", "Tracking Number", "Shipment ID")
dropdown.current(0)
dropdown.place(x=480, y=20, height=30)
searchBtn = Button(panel, text="Search", command=search, font=("Minion Pro Regular", 16, "bold"), bd=0)
searchBtn.place(x=700, y=20, height=30)

result = Frame(root, bd=0)
result.place(x=0, y=0, width=0, height=0)

root.mainloop()