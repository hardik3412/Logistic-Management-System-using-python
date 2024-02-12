# %%
from tkinter import *
from PIL import ImageTk
import os

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.bg = ImageTk.PhotoImage(file="103.jpeg")
        self.lbl_bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="beige")
        login_frame.place(x=430, y=140, width=550, height=340)

        title = Label(text="Logistic Management System", font=("lucida handwriting", 25, "bold")).place(x=0, y=30,
                                                                                                           relwidth=1)

        btn_login=Button(login_frame,text="VIEW INVENTORY",command=self.Login,font=("Elephant",13),bg="#0077be",activebackground="#005ea6",fg="black",activeforeground="white",cursor="hand2").place(x=45,y=50,width=200,height=45)
        btn_login=Button(login_frame,text="Menu",command=self.menu,font=("Elephant",13),bg="#0077be",activebackground="#005ea6",fg="black",activeforeground="white",cursor="hand2").place(x=255,y=50,width=200,height=45)
        btn_login=Button(login_frame,text="Update",command=self.update,font=("Elephant",13),bg="#0077be",activebackground="#005ea6",fg="black",activeforeground="white",cursor="hand2").place(x=175,y=250,width=200,height=45)



        btn_login = Button(login_frame, text="ADD INVENTORY", command=self.job_registration, font=("Elephant", 13),
                           bg="#0077be", activebackground="#005ea6", fg="black", activeforeground="white",
                           cursor="hand2")
        btn_login.place(x=45, y=180, width=200, height=45)

        btn_login = Button(login_frame, text="DELETE INVENTORY", command=self.availble_jobs, font=("Elephant", 13),
                           bg="#0077be", activebackground="navy blue", fg="black", activeforeground="white",
                           cursor="hand2").place(x=255, y=180, width=230, height=45)

    def job_registration(self):
        os.system('python add_inventory.py')
        #self.root.destroy()
        #import add_inventory

    def availble_jobs(self):
        os.system('python delete_inventory.py')
        #self.root.destroy()
        #import delete_order

    def Login(self):
        os.system('python view_inventory.py')
        #self.root.destroy()
        #import view_order

    def menu(self):
        self.root.destroy()
        os.system('python Mainpage.py')
        #import Mainpage


    def update(self):
        #self.root.destroy()
        #import delete_order
        os.system('python update_inventory.py')

root = Tk()
obj = Main(root)
root.mainloop()

# %%


# %%
