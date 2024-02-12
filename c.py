from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter


class LogisticManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Logistic Management System")
        self.root.geometry("1366x768")

        # --------------------------------Variable-------------------------------------------
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()



        # --------------------------------Title Frame-----------------------------------------
        label_title = Label(self.root, text="Logistic Management System", bg="#FFFFFF", fg="black", bd=20, relief=RIDGE,
                            font=("times new roman", 20, "bold"), padx=2, pady=6)
        label_title.pack(side=TOP, fill=X)

        # -------------------------------2nd Frame-------------------------------------------
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=5, bg="floral white")
        frame.place(x=0, y=80, width=1355, height=370)

        # ----------------------------Label Frame Left (Inside 2nd frame)-------------------------------------------
        frame_in_left = LabelFrame(frame, text="Membership Information", bg="#FFE6E8", fg="green", bd=12, relief=RIDGE,
                                   font=("times new roman", 10, "bold"))
        frame_in_left.place(x=0, y=3, width=750, height=340)

        #                     #------- Fields--------

        lable_member = Label(frame_in_left, bg="#FFE6E8", text="Member Type", font=("arial", 10, "bold"), padx=2,
                             pady=1)
        lable_member.grid(row=0, column=0, sticky=W)
        com_member = ttk.Combobox(frame_in_left, font=("arial", 10, "bold"), textvariable=self.member_var, width=27,
                                  state="readonly")
        com_member["value"] = ("Admin staf", "Student", "Lecturer")
        com_member.current(0)
        com_member.grid(row=0, column=1)

        lable_PRN_no = Label(frame_in_left, bg="#FFE6E8", text="PRN No.", font=("arial", 10, "bold"), padx=2)
        lable_PRN_no.grid(row=1, column=0, sticky=W)
        txt_PRN_no = Entry(frame_in_left, font=("arial", 10, "bold"), textvariable=self.prn_var, width=27)
        txt_PRN_no.grid(row=1, column=1)

        lable_title = Label(frame_in_left, bg="#FFE6E8", text="ID No.", font=("arial", 10, "bold"), padx=2, pady=4)
        lable_title.grid(row=2, column=0, sticky=W)
        txt_title = Entry(frame_in_left, font=("arial", 10, "bold"), textvariable=self.id_var, width=29)
        txt_title.grid(row=2, column=1)

        lable_first_name = Label(frame_in_left, bg="#FFE6E8", text="First Name.", font=("arial", 10, "bold"), padx=2,
                                 pady=6)
        lable_first_name.grid(row=3, column=0, sticky=W)
        txt_first_name = Entry(frame_in_left, font=("arial", 10, "bold"), textvariable=self.firstname_var, width=29)
        txt_first_name.grid(row=3, column=1)

        lable_last_name = Label(frame_in_left, bg="#FFE6E8", text="Last Name.", font=("arial", 10, "bold"), padx=2,
                                pady=6)
        lable_last_name.grid(row=4, column=0, sticky=W)
        txt_last_name = Entry(frame_in_left, font=("arial", 10, "bold"), textvariable=self.lastname_var, width=29)
        txt_last_name.grid(row=4, column=1)

        lable_address1 = Label(frame_in_left, bg="#FFE6E8", text="Address1.", font=("arial", 10, "bold"), padx=2,
                               pady=6)
        lable_address1.grid(row=5, column=0, sticky=W)
        txt_address1 = Entry(frame_in_left, font=("arial", 10, "bold"), textvariable=self.address1_var, width=29)
        txt_address1.grid(row=5, column=1)


        lable_postcode = Label(frame_in_left, bg="#FFE6E8", text="Post Code.", font=("arial", 10, "bold"), padx=2,
                               pady=6)
        lable_postcode.grid(row=7, column=0, sticky=W)
        txt_postcode = Entry(frame_in_left, font=("arial", 10, "bold"), textvariable=self.postcode_var, width=29)
        txt_postcode.grid(row=7, column=1)

        lable_mobile = Label(frame_in_left, bg="#FFE6E8", text="Mobile No.", font=("arial", 10, "bold"), padx=2, pady=6)
        lable_mobile.grid(row=8, column=0, sticky=W)
        txt_mobile = Entry(frame_in_left, font=("arial", 10, "bold"), textvariable=self.mobile_var, width=29)
        txt_mobile.grid(row=8, column=1)



        lable_date_borrowed = Label(frame_in_left, bg="#FFE6E8", text="Date Borrowed.", font=("arial", 10, "bold"),
                                    padx=2, pady=6)
        lable_date_borrowed.grid(row=3, column=2, sticky=W)
        txt_date_borrowed = Entry(frame_in_left, font=("arial", 10, "bold"), textvariable=self.dateborrowed_var,
                                  width=29)
        txt_date_borrowed.grid(row=3, column=3)

        lable_date_due = Label(frame_in_left, bg="#FFE6E8", text="Date Due.", font=("arial", 10, "bold"), padx=2,
                               pady=6)
        lable_date_due.grid(row=4, column=2, sticky=W)
        txt_date_due = Entry(frame_in_left, font=("arial", 10, "bold"), textvariable=self.datedue_var, width=29)
        txt_date_due.grid(row=4, column=3)



        # ------------------------------Buttons Frame--------------------------------------------------
        frame_button = Frame(self.root, bd=12, relief=RIDGE, padx=10, bg="#FFE6E8")
        frame_button.place(x=0, y=450, width=1355, height=60)

        btn_add_data = Button(frame_button, command=self.add_data, text="Add Data", font=("arial", 12, "bold"),
                              width=20, bg="#3B3131", fg="white")
        btn_add_data.grid(row=0, column=0)

        btn_show_data = Button(frame_button, command=self.showData, text="Show Data", font=("arial", 12, "bold"),
                               width=20, bg="#3B3131", fg="white")
        btn_show_data.grid(row=0, column=1)

        btn_update = Button(frame_button, text="Update", command=self.update, font=("arial", 12, "bold"), width=20,
                            bg="#3B3131", fg="white")
        btn_update.grid(row=0, column=2)

        btn_delete = Button(frame_button, text="Delete", command=self.delete, font=("arial", 12, "bold"), width=20,
                            bg="#3B3131", fg="white")
        btn_delete.grid(row=0, column=3)

        btn_reset = Button(frame_button, text="Reset", command=self.reset, font=("arial", 12, "bold"), width=20,
                           bg="#3B3131", fg="white")
        btn_reset.grid(row=0, column=4)

        btn_exit = Button(frame_button, text="Exit", command=self.iExit, font=("arial", 12, "bold"), width=20,
                          bg="#3B3131", fg="white")
        btn_exit.grid(row=0, column=5)

        # ------------------------------Information Frame--------------------------------------------------
        frame_details = Frame(self.root, bd=12, relief=RIDGE, padx=10, bg="#FFE6E8")
        frame_details.place(x=0, y=510, width=1355, height=190)

        table_frame = Frame(frame_details, bd=6, relief=RIDGE, bg="powder blue")
        table_frame.place(x=0, y=2, width=1322, height=158)

        xscroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.library_table = ttk.Treeview(table_frame,
                                          column=("memebertype", "prnno", "title", "firtname", "lastname", "adress1",
                                                  "adress2", "postid", "mobile", "bookid", "booktitle", "auther",
                                                  "dateborrowed",
                                                  "datedue", "days", "latereturnfine", "dateoverdue"),
                                          xscrollcommand=xscroll.set,
                                          yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("memebertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firtname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("adress1", text="Address1")
        self.library_table.heading("adress2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("dateborrowed", text="Date Of Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("memebertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firtname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("adress1", width=100)
        self.library_table.column("adress2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)


        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="hardik", database="music")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook.get(),
            self.lateratefine_var.get(),
            self.dateoverdue.get(),
            self.finallprice.get()
        ))

        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("success", "Member has been added successfully")

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="hardik", database="music")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "update library set Member=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostId=%s, Mobile=%s, Bookid=%s, Booktitle=%s, Auther=%s, dateborrowed=%s, datedue=%s, dayasofbook=%s, latereturnfine=%s, dateoverdue=%s, finalprice=%s where PRN_NO=%s",
            (
                self.member_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.auther_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysonbook.get(),
                self.lateratefine_var.get(),
                self.dateoverdue.get(),
                self.finallprice.get(),
                self.prn_var.get()
            ))

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success", "Member has been updated")

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="hardik", database="music")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),


    def showData(self):
        self.txtbox.insert(END, "Member Type:\t\t" + self.member_var.get() + "\n")
        self.txtbox.insert(END, "PRN No:\t\t" + self.prn_var.get() + "\n")
        self.txtbox.insert(END, "ID No:\t\t" + self.id_var.get() + "\n")
        self.txtbox.insert(END, "FirstName:\t\t" + self.firstname_var.get() + "\n")
        self.txtbox.insert(END, "LastName:\t\t" + self.lastname_var.get() + "\n")
        self.txtbox.insert(END, "Address1:\t\t" + self.address1_var.get() + "\n")
        self.txtbox.insert(END, "Post Code:\t\t" + self.postcode_var.get() + "\n")
        self.txtbox.insert(END, "Mobile No:\t\t" + self.mobile_var.get() + "\n")
        self.txtbox.insert(END, "DateBorrowed:\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtbox.insert(END, "DateDue:\t\t" + self.datedue_var.get() + "\n")


    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library management System", "Do you want to exit")
        if iExit > 0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "First Select the Member")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="hardik", database="music")

            my_cursor = conn.cursor()
            query = "delete from library where PRN_NO=%s"
            value = (self.prn_var.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success", "Memeber has been Deleted")


if __name__ == "__main__":
    root = Tk()
    obj = LogisticManagementSystem(root)
    root.mainloop()