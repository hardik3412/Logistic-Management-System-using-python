from tkinter import *
from LogMSysLogin import *
from LogMSysLogin import *
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='log',user='root',password='hardik')
cursor=conn.cursor()

class signup:
    def __init__(self,root):
        self.root = root
        self.f=Frame(root.title("Signup Page"),height=700,width=600,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()

        self.n1=Label(text='Name:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n2=Label(text='EMP ID:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n3=Label(text='Password:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n4=Label(text='Confirm Password:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n7=Label(text='Phone no:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n8=Label(text='Email ID:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n9=Label(text='Employee ID:',fg="black",bg="dodgerblue3",font=('Calibri',14))

        self.b1=Button(text='Sign Up',fg='white',bg='dark red',width=20,height=2,command=lambda: self.buttonclick(0))
        #self.b2=Button(text='Login', fg='white', bg='dark red', width=20, height=2,command=lambda: self.buttonclick(0))

        
        self.e1=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e2=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e3=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e4=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e5=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e6=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e7=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))

            
            
        self.n1.place(x=50,y=50)
        self.e1.place(x=250,y=50)
        self.n2.place(x=50,y=100)
        self.e2.place(x=250,y=100)
        self.n3.place(x=50,y=150)
        self.e3.place(x=250,y=150)
        self.n4.place(x=50,y=200)
        self.e4.place(x=250,y=200)
        self.n7.place(x=50,y=250)
        self.e5.place(x=250,y=250)
        self.n8.place(x=50,y=300)
        self.e6.place(x=250,y=300)
        self.n9.place(x=50,y=350)
        self.e7.place(x=250,y=350)
        

        self.b1.place(x=300,y=450)
        #self.b2.place(x=350, y=450)

    def buttonclick(self,num):

        # Check phone number field
        phone_no = self.e5.get()
        if not phone_no:
            errors.append("Phone no field is empty")
        elif not phone_no.isdigit():
            errors.append("Phone no must be a number")

        # Check email field
        email = self.e6.get()
        if not email:
            errors.append("Email ID field is empty")
        elif "@" not in email or "." not in email:
            errors.append("Email ID is not valid")

        # Check employee ID field
        emp_id2 = self.e7.get()
        if not emp_id2:
            errors.append("Employee ID field is empty")

        # Check password fields
        password = self.e3.get()
        confirm_password = self.e4.get()
        if not password:
            errors.append("Password field is empty")
        elif len(password) < 8:
            errors.append("Password must be at least 8 characters long")
        elif password != confirm_password:
            errors.append("Passwords do not match")

        # Check EMP ID field
        emp_id = self.e2.get()
        if not emp_id:
            errors.append("EMP ID field is empty")


        # Check name field
        name = self.e1.get()
        if not name:
            errors.append("Name field is empty")

        # Validate inputs
        errors = []
        
        if(self.e4.get()!=self.e3.get()):
            self.n5=Label(text='Password did not match',font=('Calibri',14),fg='red')
            self.n5.place(x=50,y=400)
            num=1
        """else:
            self.n5=Label(text=' '*46,font=('Calibri',14),fg='red')
            self.n5.place(x=50,y=350)
            
         """   
        print(num)    
        a=self.e1.get()
        b=self.e2.get()
        c=self.e3.get()
        d=self.e5.get()
        e=self.e6.get()
        x=self.e7.get()

        if(num==0):
            sql_insert_query = " insert into info VALUES (%s,%s,%s,%s,%s,%s)"

            insert_tuple_1 = (a, b, c, d, e, x)


            cursor.execute(sql_insert_query, insert_tuple_1)
            self.root.destroy()
            SEPM_LIB_LG()
            conn.commit()
            cursor.close()
            conn.close()

        else:
            return 

            
def SEPM_LIB_SNP():
    root=Tk()

    mb=signup(root)

    root.mainloop()
