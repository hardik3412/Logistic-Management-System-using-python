# importing modules
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import socket
import requests
import bs4
import mysql.connector
import re
import matplotlib.pyplot as plt

# Main Window
root = Tk()
root.title("Student Management System")
root.geometry("425x550+400+80")
root.iconbitmap("images/Vexels-Office-Bulb.ico")
root.resizable(False, False)

re_1 = re.compile(r"(\b100\b|\b[1-9][0-9]?\b)")
re_2 = re.compile(r"[a-zA-z]{2,25}(\s[a-zA-z]{2,25})?")


def get_temperature():
    try:
        city = "Mumbai"
        socket.create_connection(("www.google.com", 80))
        a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
        a2 = "&q=" + city
        a3 = "&appid=c6e315d09197cec231495138183954bd"

        api_address = a1 + a2 + a3
        res1 = requests.get(api_address)
        # print(res1)

        j1 = res1.json()
        # print(j1)

        d1 = j1['main']
        # print(d1)
        temp = d1['temp']
        # print("Temp : ", temp)
    except OSError:
        print("Check network")
    return temp


def get_quote():
    res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
    # print(res)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    quote = soup.find('img', {"class": "p-qotd"})
    # print(quote)
    text = quote['alt']
    if len(text) > 63:
        return text[:63], "-" + text[63:]
    else:
        return text, ""


def add():
    add.deiconify()
    root.withdraw()


def update():
    update.deiconify()
    root.withdraw()


def delete():
    delete.deiconify()
    root.withdraw()


def graph():
    graph.deiconify()
    root.withdraw()


def view():
    view.deiconify()
    root.withdraw()
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hardik",
            database="lms"
        )
        my_cursor = mydb.cursor()
        sql = "SELECT * FROM students ORDER BY rollno"
        my_cursor.execute(sql)
        data = my_cursor.fetchall()
        mdata = ""
        st.delete('1.0', END)
        for d in data:
            mdata = mdata + str(d[0]) + " " + str(d[1]) + " " + str(d[2]) + "\n"
        st.insert(INSERT, mdata)
        mydb.commit()
        mydb.close()
    except mysql.connector.errors as e:
        mydb.rollback()
        mydb.close()
        messagebox.showerror("Database error", e)


spacelabel = Label(root, text="")
mainframe = LabelFrame(root, padx=125, pady=50, bg="#fce38a")
mainframe.grid(row=1, column=1, padx=15)
spacelabel.grid(row=0, column=1)

add_button = Button(mainframe, text=" Add ", command=add, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                    font=('ariel', 12), activebackground="#f38181")
view_button = Button(mainframe, text=" View ", command=view, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                     font=('ariel', 12), activebackground="#f38181")
upadate_button = Button(mainframe, text="Update", command=update, pady=10, padx=36, fg="#000000", bg="#ecfbfc",
                        font=('ariel', 12), activebackground="#f38181")
delete_button = Button(mainframe, text="Delete", command=delete, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                       font=('ariel', 12), activebackground="#f38181")
graph_button = Button(mainframe, text="Graph", command=graph, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                      font=('ariel', 12), activebackground="#f38181")
q1, q2 = get_quote()
quote1 = Label(root, text=q1, font=('ariel', 10), bd=1, anchor=W)
quote2 = Label(root, text=q2, font=('ariel', 10), bd=1, anchor=W)
temp = Label(root, text="Temperature: {} ".format(get_temperature()) + u"\N{DEGREE SIGN}" + "C", font=('ariel', 12),
             bd=1, anchor=W)

add_button.grid(row=0, column=1, pady=10)
view_button.grid(row=1, column=1, pady=10)
upadate_button.grid(row=2, column=1, pady=10)
delete_button.grid(row=3, column=1, pady=10)
graph_button.grid(row=4, column=1, pady=10)
quote1.grid(row=6, column=1, sticky=W + E, padx=10, pady=1)
quote2.grid(row=7, column=1, sticky=W + E, padx=10, pady=1)
temp.grid(row=5, column=1, sticky=W + E, padx=10, pady=5)

# Add window
add = Toplevel(root)
add.title("Add student")
add.geometry("425x550+400+80")
add.iconbitmap("images/Vexels-Office-Bulb.ico")
add.resizable(False, False)
add.withdraw()

lblEid = Label(add, text="Enter student's rollno", font=('ariel', 12))
entEid = Entry(add, bd=5)

lblEname = Label(add, text="Enter student's name", font=('ariel', 12))
entEname = Entry(add, bd=5)

lblMarks = Label(add, text="Enter student's Marks", font=('ariel', 12))
entmarks = Entry(add, bd=5)


def addstudent():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="SMS"
        )
        my_cursor = mydb.cursor()
        eid = entEid.get()
        ename = entEname.get()
        marks = entmarks.get()
        if re_1.fullmatch(eid) and re_1.fullmatch(marks) and re_2.fullmatch(ename):
            sql = "INSERT INTO students VALUES(%d, '%s', %d)"
            data = (int(eid), ename, int(marks))
            my_cursor.execute(sql % data)
            mydb.commit()
            messagebox.showinfo("successful", "Added student to the database")
            entEid.delete(0, END)
            entEname.delete(0, END)
            entmarks.delete(0, END)
        else:
            message = """
                    Roll no should be a integer between 1 and 100
                    Name should contain only characters and spaces
                    Marks should be a integer between 1 and 100
                    """
            messagebox.showerror("Validation Error", message)

    except mysql.connector.errors.IntegrityError:
        mydb.rollback()
        messagebox.showerror("Error", "Student with the roll no {} already exists".format(eid))
    except Exception as e:
        mydb.rollback()
        messagebox.showerror("Error", e)


add_save = Button(add, text="Save", command=addstudent, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                  font=('ariel', 12), activebackground="#f38181")


def back():
    entEid.delete(0, END)
    entEname.delete(0, END)
    entmarks.delete(0, END)
    root.deiconify()
    add.withdraw()


add_back = Button(add, text="Back", command=back, pady=10, padx=40, fg="#000000", bg="#ecfbfc", font=('ariel', 12),
                  activebackground="#f38181")
lblEid.pack(pady=10)
entEid.pack(pady=10)
lblEname.pack(pady=10)
entEname.pack(pady=10)
lblMarks.pack(pady=10)
entmarks.pack(pady=10)
add_save.pack(pady=10)
add_back.pack(pady=10)

# Update window
update = Toplevel(root)
update.title("Update Students Data")
update.geometry("425x550+400+80")
update.iconbitmap("images/Vexels-Office-Bulb.ico")
update.resizable(False, False)
update.withdraw()

update_id = Label(update, text="Enter student's rollno", font=("ariel", 12))
updateEid = Entry(update, bd=5)

update_name = Label(update, text="Enter student's name", font=("ariel", 12))
updateName = Entry(update, bd=5)

update_marks = Label(update, text="Enter student's Marks", font=("ariel", 12))
updateMarks = Entry(update, bd=5)


def update_student():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="SMS"
        )
        my_cursor = mydb.cursor()
        eid = updateEid.get()
        ename = updateName.get()
        marks = updateMarks.get()
        print(eid)
        print(ename)
        print(marks)
        if re_1.fullmatch(eid) and re_1.fullmatch(marks) and re_2.fullmatch(ename):
            sql = "SELECT * FROM students WHERE rollno = %d"
            data = (int(eid))
            my_cursor.execute(sql % data)
            if my_cursor.fetchall():
                sql = "UPDATE students SET name = '%s',marks = %d WHERE rollno = %d"
                data = (ename, int(marks), int(eid))
                my_cursor.execute(sql % data)
                messagebox.showinfo("Successful", "Successfully updated data")
                mydb.commit()
                updateEid.delete(0, END)
                updateName.delete(0, END)
                updateMarks.delete(0, END)
            else:
                messagebox.showerror("Error", "Student with rollno {} does not exist".format(data))
                updateEid.delete(0, END)
        else:
            message = """
                    Roll no should be a integer between 1 and 100
                    Name should contain only characters and spaces
                    Marks should be a integer between 1 and 100
                    """
            messagebox.showerror("Validation Error", message)
    except Exception as e:
        mydb.rollback()
        messagebox.showerror("Error", e)


update_save = Button(update, text="Save", command=update_student, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                     font=('ariel', 12), activebackground="#f38181")


def update_back():
    updateEid.delete(0, END)
    updateName.delete(0, END)
    updateMarks.delete(0, END)
    root.deiconify()
    update.withdraw()


update_back = Button(update, text="Back", command=update_back, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                     font=('ariel', 12), activebackground="#f38181")
update_id.pack(pady=10)
updateEid.pack(pady=10)
update_name.pack(pady=10)
updateName.pack(pady=10)
update_marks.pack(pady=10)
updateMarks.pack(pady=10)
update_save.pack(pady=10)
update_back.pack(pady=10)

# delete window
delete = Toplevel(root)
delete.title("Delete Students Data")
delete.geometry("425x550+400+80")
delete.iconbitmap("images/Vexels-Office-Bulb.ico")
delete.resizable(False, False)
delete.withdraw()

delete_id = Label(delete, text="Enter student rollno", font=('ariel', 12))
deleteEid = Entry(delete, bd=5)


def delete_student():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="SMS"
        )
        my_cursor = mydb.cursor()
        eid = deleteEid.get()
        if re_1.fullmatch(eid):
            sql = "SELECT * FROM students WHERE rollno = %d"
            data = (int(eid))
            my_cursor.execute(sql % data)
            if my_cursor.fetchall():
                sql = "DELETE FROM students WHERE rollno = %d"
                data = (int(eid))
                my_cursor.execute(sql % data)
                mydb.commit()
                messagebox.showinfo("successful", "Successfully deleted")
                deleteEid.delete(0, END)
            else:
                messagebox.showerror("Error", "Student with rollno {} does not exist".format(data))
                updateEid.delete(0, END)
        else:
            message = "Roll no should be a integer between 1 and 100"
            messagebox.showerror("Validation Error", message)
    except Exception as e:
        mydb.rollback()
        messagebox.showerror("Error", e)

    print(eid)


delete_save = Button(delete, text="Delete", command=delete_student, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                     font=('ariel', 12), activebackground="#f38181")


def delete_back():
    deleteEid.delete(0, END)
    root.deiconify()
    delete.withdraw()


delete_back = Button(delete, text="Back", command=delete_back, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                     font=('ariel', 12), activebackground="#f38181")

delete_id.pack(pady=10)
deleteEid.pack(pady=10)

delete_save.pack(pady=10)
delete_back.pack(pady=10)

# View Window
view = Toplevel(root)
view.title("Get stats")
view.geometry("425x550+400+80")
view.iconbitmap("images/Vexels-Office-Bulb.ico")
view.resizable(False, False)
view.withdraw()


# to go back to the main window
def f4():
    st.delete(1.0, END)
    root.deiconify()
    view.withdraw()


st = scrolledtext.ScrolledText(view, width=30, height=10, font=('ariel', 10))

btnViewBack = Button(view, text="Back", command=f4, pady=10, padx=40, fg="#000000", bg="#ecfbfc", font=('ariel', 12),
                     activebackground="#f38181")

st.pack(pady=10)
btnViewBack.pack(pady=10)

# Graph
graph = Toplevel(root)
graph.title("Student Management System")
graph.geometry("425x550+400+80")
graph.iconbitmap("images/Vexels-Office-Bulb.ico")
graph.resizable(False, False)
graph.withdraw()


def getData():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hardik",
            database="lms"
        )
        my_cursor = mydb.cursor()
        sql = "SELECT * FROM students ORDER BY rollno"
        my_cursor.execute(sql)
        data = my_cursor.fetchall()
        r = []
        n = []
        m = []
        for roll_number, name, marks in data:
            r.append(roll_number)
            n.append(name)
            m.append(marks)
        return r, n, m


    except mysql.connector.errors as e:
        mydb.rollback()
        mydb.close()
        messagebox.showerror("Database error", e)


def line():
    rollno, names, marks = getData()
    plt.plot(names, marks, label="Marks")
    plt.title("Students Details")
    plt.xlabel("Students name")
    plt.ylabel("Marks")
    plt.grid()
    plt.show()


def bar():
    rollno, names, marks = getData()
    plt.bar(names, marks)
    plt.title("Students scores", fontsize=20)
    plt.xlabel("Students name", fontsize=15)
    plt.ylabel("Students marks", fontsize=15)
    plt.grid()
    plt.show()


def graph_back():
    root.deiconify()
    graph.withdraw()


frame_graph = LabelFrame(graph, padx=125, pady=50, bg="#fce38a")
frame_graph.pack(pady=20, padx=10)

line_graph = Button(frame_graph, text="Line Graph", command=line, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                    font=('ariel', 12), activebackground="#f38181")
bar_graph = Button(frame_graph, text="Bar Graph", command=bar, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                   font=('ariel', 12), activebackground="#f38181")
back_graph = Button(frame_graph, text="Back", command=graph_back, pady=10, padx=40, fg="#000000", bg="#ecfbfc",
                    font=('ariel', 12), activebackground="#f38181")

line_graph.pack(pady=10)
bar_graph.pack(pady=10)
back_graph.pack(pady=10)

root.mainloop()