# %%
import os
from tkinter import *
from PIL import ImageTk


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

        btn_login=Button(login_frame,text="Tracking",command=self.tracking,font=("Elephant",13),bg="#0077be",activebackground="#005ea6",fg="black",activeforeground="white",cursor="hand2").place(x=45,y=50,width=200,height=45)
        btn_login=Button(login_frame,text="Report",command=self.report,font=("Elephant",13),bg="#0077be",activebackground="#005ea6",fg="black",activeforeground="white",cursor="hand2").place(x=255,y=50,width=200,height=45)


        btn_login = Button(login_frame, text="Order Management", command=self.job_registration, font=("Elephant", 13),
                           bg="#0077be", activebackground="#005ea6", fg="black", activeforeground="white",
                           cursor="hand2")
        btn_login.place(x=45, y=180, width=200, height=45)

        btn_login = Button(login_frame, text="Inventory", command=self.availble_jobs, font=("Elephant", 13),
                           bg="#0077be", activebackground="navy blue", fg="black", activeforeground="white",
                           cursor="hand2").place(x=255, y=180, width=200, height=45)

    def job_registration(self):
        self.root.destroy()
        import order_page

    def availble_jobs(self):
        self.root.destroy()
        import inventory_page

    def tracking(self):
        self.root.destroy()
        import tracking_page

    def report(self):
        #self.root.destroy()
        os.system("python date_tracking.py")


root = Tk()
obj = Main(root)
root.mainloop()

# %%


# %%
