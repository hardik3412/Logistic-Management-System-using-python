# %%
from tkinter import *
from PIL import ImageTk
import os

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.bg = ImageTk.PhotoImage(file="103.jpeg")
        self.lbl_bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="beige")
        login_frame.place(x=430, y=140, width=550, height=340)

        title = Label(text="Logistic Management System", font=("lucida handwriting", 25, "bold")).place(x=0, y=30,
                                                                                                           relwidth=1)


        btn_login = Button(login_frame, text="Add Tracking", command=self.job_registration, font=("Elephant", 13),
                           bg="#0077be", activebackground="#005ea6", fg="black", activeforeground="white",
                           cursor="hand2")
        btn_login.place(x=45, y=180, width=200, height=45)
        btn_login=Button(login_frame,text="Report",command=self.report,font=("Elephant",13),bg="#0077be",activebackground="#005ea6",fg="black",activeforeground="white",cursor="hand2").place(x=45,y=50,width=200,height=45)


        btn_login=Button(login_frame,text="Menu",command=self.menu,font=("Elephant",13),bg="#0077be",activebackground="#005ea6",fg="black",activeforeground="white",cursor="hand2").place(x=255,y=50,width=200,height=45)


        btn_login = Button(login_frame, text="View Tracking", command=self.availble_jobs, font=("Elephant", 13),
                           bg="#0077be", activebackground="navy blue", fg="black", activeforeground="white",
                           cursor="hand2").place(x=255, y=180, width=200, height=45)

    def job_registration(self):
        os.system('python add_tracking.py')
        #self.root.destroy()
        #import add_tracking

    def availble_jobs(self):
        #self.root.destroy()
        os.system('python view_tracking.py')

        #import inventory_page

    def menu(self):
        self.root.destroy()
        os.system('python Mainpage.py')
        #import Mainpage

    def report(self):
        os.system('python jointtracking.py')
        #self.root.destroy()
        #import add_tracking



root = Tk()
obj = Main(root)
root.mainloop()

