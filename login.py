# %%
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
        login_frame.place(x=490, y=200, width=470, height=300)

        title = Label(text="Logistic Management System", font=("lucida handwriting", 25, "bold")).place(x=0, y=30,
                                                                                                           relwidth=1)

        # btn_login=Button(login_frame,text="Log In",command=self.Login,font=("Elephant",13),bg="sky blue",activebackground="sky blue",fg="white",activeforeground="white",cursor="hand2").place(x=45,y=50,width=250,height=45)

        btn_login = Button(login_frame, text="Login", command=self.job_registration, font=("Elephant", 13),
                           bg="#0077be", activebackground="#005ea6", fg="black", activeforeground="white",
                           cursor="hand2")
        btn_login.place(x=135, y=120, width=200, height=45)

        btn_login = Button(login_frame, text="Signup", command=self.availble_jobs, font=("Elephant", 13),
                           bg="#0077be", activebackground="navy blue", fg="black", activeforeground="white",
                           cursor="hand2").place(x=135, y=180, width=200, height=45)

    def job_registration(self):
        self.root.destroy()
        import a

    def availble_jobs(self):
        self.root.destroy()
        #import availablejobs

    # def Login(self):
    # self.root.destroy()
    # import Loginwindow


root = Tk()
obj = Main(root)
root.mainloop()

# %%


# %%
