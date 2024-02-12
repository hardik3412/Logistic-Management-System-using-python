from tkinter import *
from tkinter import ttk
import mysql.connector
import os
from tkinter import messagebox

class jobs:
    def __init__(self, root):
        self.root = root
        self.root.title("Available Jobs")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="JOB POSTED BY RECRUITER", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="dark slate grey", fg="black")
        title.pack(side=TOP, fill=X)

        # =======All variables=======
        self.Job_var = StringVar()
        self.title_var = StringVar()
        self.Salary_var = StringVar()
        self.Qualifi_var = StringVar()
        self.Department_var = StringVar()
        self.A_var = StringVar()
        self.B_var = StringVar()
        self.C_var = StringVar()

        self.Search_by = StringVar()
        self.Search_txt = StringVar()

        # =========manage frame======
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="pink1")
        Manage_Frame.place(x=20, y=100, width=450, height=600)

        m_title = Label(Manage_Frame, text="JOB DESCRIPTION", bg="IndianRed1", fg="black",
                        font=("Microsoft Yahei UI LIGHT", 24, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        lbl_Job = Label(Manage_Frame, text="job :", bg="royal blue", fg="white", font=("Microsoft Yahei UI LIGHT"
                                                                                            , 15, "bold"))
        lbl_Job.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Job = Entry(Manage_Frame, textvariable=self.Job_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5,
                        relief=GROOVE)
        txt_Job.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_Company = Label(Manage_Frame, text="Company :", bg="royal blue", fg="white",
                            font=("Microsoft Yahei UI LIGHT", 15, "bold"))
        lbl_Company.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Company = Entry(Manage_Frame, textvariable=self.title_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5,
                            relief=GROOVE)
        txt_Company.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Salary = Label(Manage_Frame, text="Salary :", bg="royal blue", fg="white",
                           font=("Microsoft Yahei UI LIGHT", 18, "bold"))
        lbl_Salary.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Salary = Entry(Manage_Frame, textvariable=self.Salary_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5,
                           relief=GROOVE)
        txt_Salary.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Qualifi = Label(Manage_Frame, text="Qualification:", bg="royal blue", fg="white",
                            font=("Microsoft Yahei UILIGHT", 15, "bold"))
        lbl_Qualifi.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_Qualifi = Entry(Manage_Frame, textvariable=self.Qualifi_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"),
                            bd=5,
                            relief=GROOVE)
        txt_Qualifi.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_Department = Label(Manage_Frame, text="Department:", bg="royal blue", fg="white",
                               font=("Microsoft Yahei UI LIGHT", 15, "bold"))
        lbl_Department.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Department = Entry(Manage_Frame, textvariable=self.Department_var,
                               font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5,
                               relief=GROOVE)
        txt_Department.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_A = Label(Manage_Frame, text="A:", bg="royal blue", fg="white",
                      font=("Microsoft Yahei UI LIGHT", 15, "bold"))
        lbl_A.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_A = Entry(Manage_Frame, textvariable=self.A_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5,
                      relief=GROOVE)
        txt_A.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_B = Label(Manage_Frame, text="B:", bg="royal blue", fg="white",
                      font=("Microsoft Yahei UI LIGHT", 15, "bold"))
        lbl_B.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_B = Entry(Manage_Frame, textvariable=self.B_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5,
                      relief=GROOVE)
        txt_B.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_C = Label(Manage_Frame, text="C:", bg="royal blue", fg="white",
                      font=("Microsoft Yahei UI LIGHT", 15, "bold"))
        lbl_C.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        txt_C = Entry(Manage_Frame, textvariable=self.C_var, font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5,
                      relief=GROOVE)
        txt_C.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        # =========Button frame======
        Btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="pink1")
        Btn_Frame.place(x=10, y=500, width=420)

        Addbtn = Button(Btn_Frame, text="Add", width=10, command=self.add_job)
        Addbtn.grid(row=0, column=0, padx=10, pady=10)

        Updatebtn = Button(Btn_Frame, text="Update", width=10, command=self.update_job)
        Updatebtn.grid(row=0, column=1, padx=10, pady=10)

        Deletebtn = Button(Btn_Frame, text="Delete", width=10, command=self.delete_job)
        Deletebtn.grid(row=0, column=2, padx=10, pady=10)

        Clearbtn = Button(Btn_Frame, text="Clear", width=10, command=self.clear_fields)
        Clearbtn.grid(row=0, column=3, padx=10, pady=10)

        # =========Detail frame======
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="pink1")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        lbl_Search = Label(Detail_Frame, text="Search By:", bg="royal blue", fg="white",
                           font=("Microsoft Yahei UI LIGHT", 15, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search = ttk.Combobox(Detail_Frame, font=("Microsoft Yahei UI LIGHT", 12, "bold"), state='readonly',
                                    width=10)
        combo_Search['values'] = ("job", "Job_Title", "Qualification", "Department")
        combo_Search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_Search = Entry(Detail_Frame, font=("Microsoft Yahei UI LIGHT", 12, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_job)
        Searchbtn.grid(row=0, column=3, padx=10, pady=10)

        Showallbtn = Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch_jobs)
        Showallbtn.grid(row=0, column=4, padx=10, pady=10)

        # =========Table frame======
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="pink1")
        Table_Frame.place(x=10, y=70, width=770, height=500)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        self.job_table = ttk.Treeview(Table_Frame,
                                      columns=("job", "title", "qualifi", "department","salary", "a", "b", "c"),
                                      xscrollcommand=scroll_x.set,
                                      yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.job_table.xview)
        scroll_y.config(command=self.job_table.yview)

        self.job_table.heading("job", text="job")
        self.job_table.heading("title", text="title")
        self.job_table.heading("qualifi", text="Qualification")
        self.job_table.heading("department", text="Department")
        self.job_table.heading("salary", text="salary")
        self.job_table.heading("a", text="A")
        self.job_table.heading("b", text="B")
        self.job_table.heading("c", text="C")

        self.job_table['show'] = 'headings'

        self.job_table.column("job", width=50)
        self.job_table.column("title", width=100)
        self.job_table.column("qualifi", width=100)
        self.job_table.column("department", width=100)
        self.job_table.column("salary", width=100)
        self.job_table.column("a", width=50)
        self.job_table.column("b", width=50)
        self.job_table.column("c", width=50)
        self.job_table.pack(fill=BOTH, expand=1)
        self.job_table.bind("<ButtonRelease-1>", self.get_job_data)
        self.fetch_jobs()

    def add_job(self):
        job = self.txt_job.get()
        title = self.txt_title.get()
        qualification = self.txt_qualification.get()
        department = self.txt_department.get()
        salary = self.txt_salary.get()
        a = self.txt_a.get()
        b = self.txt_b.get()
        c = self.txt_c.get()

        if job == "" or title == "" or qualification == "" or department == "" or salary =="" or a == "" or b == "" or c == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            query = "INSERT INTO jobs (job, title, qualification, department,salary, a, b, c) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (job, title, qualification, department,salary, a, b, c)
            self.execute_query(query, values)
            self.clear_fields()
            self.fetch_jobs()
            messagebox.showinfo("Success", "Job added successfully!")

    def update_job(self):
        job = self.txt_job.get()
        title = self.txt_title.get()
        qualification = self.txt_qualification.get()
        department = self.txt_department.get()
        salary = self.txt_salary.get()
        a = self.txt_a.get()
        b = self.txt_b.get()
        c = self.txt_c.get()

        if job == "":
            messagebox.showerror("Error", "Please select a job to update!")
        else:
            query = "UPDATE jobs SET title=%s, qualification=%s, department=%s,salary=%s, a=%s, b=%s, c=%s WHERE job=%s"
            values = (title, qualification, department,salary, a, b, c, job)
            self.execute_query(query, values)
            self.clear_fields()
            self.fetch_jobs()
            messagebox.showinfo("Success", "Job updated successfully!")

    def delete_job(self):
        job = self.txt_job.get()

        if job == "":
            messagebox.showerror("Error", "Please select a job to delete!")
        else:
            result = messagebox.askquestion("Confirmation", "Are you sure you want to delete this job?",
                                            icon="warning")
            if result == "yes":
                query = "DELETE FROM jobs WHERE job = %s"
                values = (job,)
                self.execute_query(query, values)
                self.clear_fields()
                self.fetch_jobs()
                messagebox.showinfo("Success", "Job deleted successfully!")

    def clear_fields(self):
        self.txt_job.delete(0, END)
        self.txt_title.delete(0, END)
        self.txt_qualification.delete(0, END)
        self.txt_department.delete(0, END)
        self.txt_salary.delete(0, END)
        self.txt_a.delete(0, END)
        self.txt_b.delete(0, END)
        self.txt_c.delete(0, END)

    def fetch_jobs(self):
        query = "SELECT * FROM jobs"
        jobs = self.execute_query(query)
        self.job_table.delete(*self.job_table.get_children())
        if jobs:
            for job in jobs:
                self.job_table.insert('', END, values=job)

    def search_job(self):
        selected_column = self.combo_Search.get()
        search_query = self.txt_Search.get()
        query = f"SELECT * FROM jobs WHERE {selected_column} LIKE '%{search_query}%'"
        jobs = self.execute_query(query)
        self.job_table.delete(*self.job_table.get_children())
        if jobs:
            for job in jobs:
                self.job_table.insert('', END, values=job)

    def get_job_data(self, event):
        selected_row = self.job_table.focus()
        data = self.job_table.item(selected_row)
        row = data['values']
        self.txt_job.delete(0, END)
        self.txt_job.insert(END, row[0])
        self.txt_title.delete(0, END)
        self.txt_title.insert(END, row[1])
        self.txt_qualification.delete(0, END)
        self.txt_qualification.insert(END, row[2])
        self.txt_department.delete(0, END)
        self.txt_department.insert(END, row[3])
        self.txt_salary.delete(0, END)
        self.txt_salary.insert(END, row[4])
        self.txt_a.delete(0, END)
        self.txt_a.insert(END, row[5])
        self.txt_b.delete(0, END)
        self.txt_b.insert(END, row[6])
        self.txt_c.delete(0, END)
        self.txt_c.insert(END, row[7])

    def execute_query(self, query, values=None):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hardik",
            database="jobportal"
        )
        cursor = db.cursor()
        try:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            db.commit()
            return cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Error", f"Error executing query: {e}")
        finally:
            cursor.close()
            db.close()

root = Tk()
obj = jobs(root)
root.mainloop()