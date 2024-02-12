from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime
# import time
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import re
from dateutil.relativedelta import relativedelta

loginWindowPanel = ''
registrationPagePanel = ''
criminalPanel = ''


# Login page function window code

def loginpagePanel():
    loginWindowPanel = Tk()  # instantiation of a window
    loginWindowPanel.geometry("370x300")
    loginWindowPanel.configure(background="#b3d1ff")
    loginWindowPanel.title("Login Page")

    # Login label like title
    lbllogin = Label(loginWindowPanel,
                     text="Login Page",
                     font=("Times New Roman", 25),
                     background="#b3d1ff")
    lbllogin.grid(column=0, row=0, columnspan=3, pady=10, padx=10)
    # lbllogin.config(background="black", foreground="white")

    # user label and entry
    userlbl = Label(loginWindowPanel,
                    text="Username",
                    font=("Times New Roman", 15),
                    background="#b3d1ff")
    userlbl.grid(column=0, row=1, padx=5, pady=10)

    userentry = Entry(loginWindowPanel,
                      font=("Times New Roman", 15))
    userentry.grid(column=1, row=1)

    # Password label and entry
    psdlabel = Label(loginWindowPanel,
                     text="Password",
                     font=("Times New Roman", 15),
                     background="#b3d1ff")
    psdlabel.grid(column=0, row=2, padx=5, pady=10)

    # paswd_str = StringVar()
    psdentry = Entry(loginWindowPanel,
                     show="*",
                     font=("Times New Roman", 15))
    psdentry.grid(column=1, row=2)

    checkbtnVar = IntVar(value=0)

    def show_pswsd():
        if (checkbtnVar.get() == 1):
            psdentry.config(show='')
            # checkbtnVar.set(value=1)
        else:
            psdentry.config(show='*')
            # checkbtnVar.set(value=0)

    checkbtn = Checkbutton(loginWindowPanel,
                           text="Show Password",
                           font=("Times New Roman", 10),
                           offvalue=0,
                           onvalue=1,
                           variable=checkbtnVar,
                           command=show_pswsd,
                           background="#b3d1ff")
    checkbtn.grid(column=0, row=3, columnspan=2, padx=5, pady=10)

    # Login button and create account button

    submitbtn = Button(loginWindowPanel,
                       text="Submit",
                       font=("Times New Roman", 16),
                       command=lambda: validatePage(userentry.get(), psdentry.get()))
    submitbtn.grid(column=0, row=4, padx=5, pady=10)

    signUpbtn = Button(loginWindowPanel,
                       text="Sign Up",
                       font=("Times New Roman", 16),
                       command=lambda: registrationPage(loginWindowPanel))
    signUpbtn.grid(column=1, row=4, rowspan=2, padx=5, pady=10)

    def validatePage(userentry, psdentry):
        if (len(userentry) != 0 and len(psdentry) != 0):
            try:
                connection = mysql.connector.connect(host="localhost",
                                                     database="criminalmanagement",
                                                     user="root",
                                                     password="Levi@8355")
                fetchData = f"""select policeIncharge, username, paswd_field from policerecord where username = '{userentry}'"""
                cursor = connection.cursor()
                cursor.execute(fetchData)
                record = cursor.fetchone()
            except Error as e:
                messagebox.showerror("Error", "While connecting to database ", e)
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("Mysql connnection is closed.")

            if (record != None):
                if (record[2] == psdentry):
                    inchargename = record[0]
                    polManagePanel(userentry, psdentry, inchargename, loginWindowPanel)

                else:
                    messagebox.showerror("Error", "Wrong password.")
            else:
                messagebox.showerror("Error", f"{userentry} This Username doesn't exists.")

        else:
            messagebox.showerror("Failed", "Both Fields are mandatory")

    # submitbtn.config(command=popupDetails)
    loginWindowPanel.mainloop()


# Registration page function

def registrationPage(loginWindowPanel):
    loginWindowPanel.iconify()
    registrationPagePanel = Toplevel(loginWindowPanel)
    registrationPagePanel.geometry("525x575")
    registrationPagePanel.configure(background="#b3d1ff")
    registrationPagePanel.title("Registration Panel")
    # registrationPagePanel.config(background="black")

    registerLabel = Label(registrationPagePanel,
                          text="Registration Page for Police",
                          font=("Times New Roman", 25),
                          background="#b3d1ff")
    registerLabel.grid(column=0, row=0, columnspan=3, padx=50)

    # Police incharge and entry
    policelbl = Label(registrationPagePanel,
                      text="Police Incharge",
                      font=("Times New Roman", 15),
                      background="#b3d1ff")
    policelbl.grid(column=0, row=1, sticky=W, padx=5, pady=10)

    policeentry = Entry(registrationPagePanel,
                        font=("Times New Roman", 15))
    policeentry.grid(column=1, row=1)

    # Station name label and entry
    stnNamelbl = Label(registrationPagePanel,
                       text="Station Name",
                       font=("Times New Roman", 15),
                       background="#b3d1ff")
    stnNamelbl.grid(column=0, row=2, sticky=W, padx=5, pady=10)
    stnEntry = Entry(registrationPagePanel,
                     font=("Times New Roman", 15))
    stnEntry.grid(column=1, row=2)

    # station id label and entry
    stnIDlbl = Label(registrationPagePanel,
                     text="Station ID",
                     font=("Times New Roman", 15),
                     background="#b3d1ff")
    stnIDlbl.grid(column=0, row=3, sticky=W, padx=5, pady=10)
    stnIDEntry = Entry(registrationPagePanel,
                       font=("Times New Roman", 15))
    stnIDEntry.grid(column=1, row=3)

    # Contact details
    mobLbl = Label(registrationPagePanel,
                   text="Mobile",
                   font=("Times New Roman", 15),
                   background="#b3d1ff")
    mobLbl.grid(column=0, row=4, sticky=W, padx=5, pady=10)
    mobEntry = Entry(registrationPagePanel,
                     font=("Times New Roman", 15))
    mobEntry.grid(column=1, row=4)

    emailLbl = Label(registrationPagePanel,
                     text="Email",
                     font=("Times New Roman", 15),
                     background="#b3d1ff")
    emailLbl.grid(column=0, row=5, sticky=W, padx=5, pady=10)
    emailEntry = Entry(registrationPagePanel,
                       font=("Times New Roman", 15))
    emailEntry.grid(column=1, row=5)

    # Incharge Address label and entry
    inAdsLabel = Label(registrationPagePanel,
                       text="Incharge Address",
                       font=("Times New Roman", 15),
                       background="#b3d1ff")
    inAdsLabel.grid(column=0, row=6, sticky=W, padx=5, pady=10)
    inadsEntry = Entry(registrationPagePanel,
                       font=("Times New Roman", 15))
    inadsEntry.grid(column=1, row=6)

    # station address label and Entry
    stnAdsLabel = Label(registrationPagePanel,
                        text="Station Address",
                        font=("Times New Roman", 15),
                        background="#b3d1ff")
    stnAdsLabel.grid(column=0, row=7, sticky=W, padx=5, pady=10)
    stnAdsEntry = Entry(registrationPagePanel,
                        font=("Times New Roman", 15))
    stnAdsEntry.grid(column=1, row=7)

    # Username label and entry
    usrnamelbl = Label(registrationPagePanel,
                       text="Username",
                       font=("Times New Roman", 15),
                       background="#b3d1ff")
    usrnamelbl.grid(column=0, row=8, sticky=W, padx=5, pady=10)
    usrEntry = Entry(registrationPagePanel,
                     font=("Times New Roman", 15))
    usrEntry.grid(column=1, row=8)

    # Password label and entry
    pswdlbl = Label(registrationPagePanel,
                    text="Password",
                    font=("Times new Roman", 15),
                    background="#b3d1ff")
    pswdlbl.grid(column=0, row=9, sticky=W, padx=5, pady=10)
    pswdEntry = Entry(registrationPagePanel,
                      font=("Times New Roman", 15),
                      show="*")
    pswdEntry.grid(column=1, row=9)

    # function and flag for show btn chck btn
    pswdcheckbtnVar = IntVar(value=0)

    def show_pswsd():
        if (pswdcheckbtnVar.get() == 1):
            pswdEntry.config(show='')
        else:
            pswdEntry.config(show='*')

    # show password radiobutton
    checkbtnShowPswd = Checkbutton(registrationPagePanel,
                                   text="Show Password",
                                   font=("Times New Roman", 10),
                                   offvalue=0,
                                   onvalue=1,
                                   variable=pswdcheckbtnVar,
                                   command=show_pswsd,
                                   background="#b3d1ff")
    checkbtnShowPswd.grid(column=1, row=10, padx=5, pady=10)

    # Create button
    regCreateBtn = Button(registrationPagePanel,
                          text="Create",
                          font=("Times New Roman", 15))
    regCreateBtn.grid(column=1,
                      row=11)

    def registeredRecords(inchargeName, stnName, stnID, mobileNO, email, inchAddress, stationAddress, username,
                          password):
        getPoliceInchargeName = inchargeName
        getStationName = stnName
        getstationId = stnID
        getMobile = mobileNO
        getemail = email
        getInchargeAddress = inchAddress
        getstationAddress = stationAddress
        getUsername = username
        getPassword = password
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='criminalmanagement',
                                                 user='root',
                                                 password='Levi@8355')
            sqlInsertQuery = f"""INSERT INTO policerecord
                    VALUES('{getPoliceInchargeName}','{getStationName}','{getstationId}',{getMobile},'{getemail}','{getInchargeAddress}','{getstationAddress}','{getUsername}','{getPassword}');
                    """
            cursor = connection.cursor()
            cursor.execute(sqlInsertQuery)
            connection.commit()
            messagebox.showinfo("Succes", "Record inserted successfully")

        except Error as e:
            messagebox.showerror("Error", f"There is error while saving record {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("mysql connnection is close")
                registrationPagePanel.destroy()
                loginWindowPanel.deiconify()

    def validatePoliceRecords(inchargeName, stnName, stnID, mobileNO, email, inchAddress, stationAddress, username,
                              password):
        getPoliceInchargeName = inchargeName
        getStationName = stnName
        getstationId = stnID
        getMobile = mobileNO
        getemail = email
        getInchargeAddress = inchAddress
        getstationAddress = stationAddress
        getUsername = username
        getPassword = password

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='criminalmanagement',
                                                 user='root',
                                                 password='Levi@8355')
            queryTogetrecord = f"""select * from policerecord where username = '{username}';"""
            cursor = connection.cursor()
            cursor.execute(queryTogetrecord)
            fetchRecord = cursor.fetchone()

        except Error as e:
            messagebox.showerror("Error", "Not able to Connect with mysql")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        if (len(getPoliceInchargeName) == 0 or len(getStationName) == 0 or len(getstationId) == 0 or len(
                getMobile) == 0 or len(getemail) == 0 or len(getemail) == 0 or len(getInchargeAddress) == 0 or len(
                getstationAddress) == 0 or len(getUsername) == 0 or len(getPassword) == 0):
            messagebox.showerror("Error", "Each and every field must be filled before submission")
        elif (fetchRecord != None):
            messagebox.showerror("Exists", f"{username} This username already exists")
        else:
            registeredRecords(inchargeName, stnName, stnID, mobileNO, email, inchAddress, stationAddress, username,
                              password)

    regCreateBtn.configure(
        command=lambda: validatePoliceRecords(policeentry.get(), stnEntry.get(), stnIDEntry.get(), mobEntry.get(),
                                              emailEntry.get(), inadsEntry.get(), stnAdsEntry.get(), usrEntry.get(),
                                              pswdEntry.get()))

    registrationPagePanel.mainloop()


def polManagePanel(username, password, inchargename, loginWindowPanel):
    messagebox.showinfo("Success", f"Successfully logged\n Welcome username: {username} password:{password}")
    criminalPanel = Toplevel(loginWindowPanel, background="#b3d1ff")
    loginWindowPanel.iconify()
    criminalPanel.state('zoomed')
    # loginWindowPanel.destroy()
    w, h = criminalPanel.winfo_screenwidth(), criminalPanel.winfo_screenheight()
    criminalPanel.geometry("%dx%d+0+0" % (w, h))
    criminalPanel.title("Criminal Records Register")

    # Title label
    criminalTitlelbl = Label(criminalPanel,
                             text="Criminal management System",
                             font=("Times New Roman", 25),
                             background="#b3d1ff")
    criminalTitlelbl.grid(row=0, column=2, columnspan=3, sticky=N)

    # Incharge label
    inchUsername = Label(criminalPanel,
                         text=f"Username: {username}",
                         font=("Times New Roman", 15),
                         background="#b3d1ff")
    inchUsername.grid(row=1, column=0, padx=5, pady=10)

    inchName = Label(criminalPanel,
                     text=f"Incharge name: {inchargename}",
                     font=("Times New Roman", 15),
                     background="#b3d1ff")
    inchName.grid(row=1, column=5, padx=5, pady=10)

    # caseId labels and entry
    caseIdLbl = Label(criminalPanel,
                      text="Case Id",
                      font=("Times New Roman", 15),
                      background="#b3d1ff")
    caseIdLbl.grid(row=2, column=0, sticky=W, padx=5)
    caseIdEntry = Entry(criminalPanel,
                        font=("Times New Roman", 15))
    caseIdEntry.grid(row=2, column=1)

    # DOB entry and labels
    doblbl = Label(criminalPanel,
                   text="DOB",
                   background="#b3d1ff",
                   font=("Times New Roman", 15))
    doblbl.grid(row=2, column=2, sticky=W, padx=5)
    dobpicker = DateEntry(criminalPanel, year=2019, month=6, day=22,
                          background='darkblue', foreground='white', borderwidth=2,
                          date_pattern='dd-mm-yyyy')
    dobpicker.grid(row=2, column=3, sticky=W)

    # father label and entry
    fatherlbl = Label(criminalPanel,
                      text="Father Name",
                      font=("Times New Roman", 15),
                      background="#b3d1ff")
    fatherlbl.grid(row=7, column=0, sticky=W, padx=5)
    fatherEntry = Entry(criminalPanel,
                        font=("Times New Roman", 15))
    fatherEntry.grid(row=7, column=1)

    # CriminalName entry and labels
    crmNamelbl = Label(criminalPanel,
                       text="Criminal Name",
                       font=("Times New Roman", 15),
                       background="#b3d1ff")
    crmNamelbl.grid(row=3, column=0, sticky=W, padx=5, pady=10)
    crmNameEntry = Entry(criminalPanel,
                         font=("Times New Roman", 15))
    crmNameEntry.grid(row=3, column=1)

    # Age label and Entry
    # derivedAge = dobpicker.get()

    ageLbl = Label(criminalPanel,
                   text="Age",
                   font=("Times New Roman", 15),
                   background="#b3d1ff")
    ageLbl.grid(row=3, column=2, sticky=W, padx=5, pady=10)
    derAgeLbl = Label(criminalPanel,
                      text="Derived",
                      font=("Times New Roman", 15),
                      background="#b3d1ff")
    derAgeLbl.grid(row=3, column=3, sticky=W)

    # Gender label and radiobutton
    genderlbl = Label(criminalPanel,
                      text="Gender",
                      font=("Times New Roman", 15),
                      background="#b3d1ff")
    genderlbl.grid(row=7, column=2, sticky=W, padx=5, pady=10)
    genderFrame = Frame(criminalPanel)
    genderFrame.grid(row=7, column=3, columnspan=3, sticky=W)

    gendervar = StringVar()
    maleradiobtn = Radiobutton(genderFrame,
                               text="Male",
                               variable=gendervar,
                               value="male",
                               background="#b3d1ff")
    maleradiobtn.grid(row=0, column=0, sticky=W)
    femaleradiobtn = Radiobutton(genderFrame,
                                 text="Female",
                                 variable=gendervar,
                                 value="female",
                                 background="#b3d1ff")
    femaleradiobtn.grid(row=0, column=1, sticky=W)

    # nick name label and entry
    nickNamelbl = Label(criminalPanel,
                        text="Nick Name",
                        font=("Times New Roman", 15),
                        background="#b3d1ff")
    nickNamelbl.grid(row=4, column=0, sticky=W, padx=5)
    nickNameEntry = Entry(criminalPanel,
                          font=("Times New Roman", 15))
    nickNameEntry.grid(row=4, column=1)
    # Crime date and its label
    crimedatelbl = Label(criminalPanel,
                         text="Crime Date",
                         font=("Times New Roman", 15),
                         background="#b3d1ff")
    crimedatelbl.grid(row=4, column=2, sticky=W, padx=5)
    crimedatePicker = DateEntry(criminalPanel, day=22, month=6, year=2019,
                                background='darkblue', foreground='white', borderwidth=2,
                                date_pattern='dd-mm-yyyy')
    crimedatePicker.grid(row=4, column=3, sticky=W)

    mwantedlbl = Label(criminalPanel,
                       text="Most Wanted",
                       font=("Times New Roman", 15),
                       background="#b3d1ff")
    mwantedlbl.grid(row=8, column=0, sticky=W, padx=5)

    # Most wanted frame
    mwantedFrame = Frame(criminalPanel)
    mwantedFrame.grid(row=8, column=1, sticky=W)

    mwantedvar = StringVar()
    yesradiobtn = Radiobutton(mwantedFrame,
                              text="Yes",
                              variable=mwantedvar,
                              value="yes",
                              background="#b3d1ff")
    yesradiobtn.grid(row=0, column=0)
    noradiobtn = Radiobutton(mwantedFrame,
                             text="No",
                             variable=mwantedvar,
                             value="no",
                             background="#b3d1ff")
    noradiobtn.grid(row=0, column=1)

    # Address fields
    addresslbl = Label(criminalPanel,
                       text="Adress",
                       font=("Times New Roman", 15),
                       background="#b3d1ff")
    addresslbl.grid(row=5, column=0, sticky=W, padx=5, pady=10)
    addressEntry = Entry(criminalPanel,
                         font=("Times New Roman", 15))
    addressEntry.grid(row=5, column=1)

    # Crime type label and entry
    crimeTypelbl = Label(criminalPanel,
                         text="Crime Type",
                         font=("Times New Roman", 15),
                         background="#b3d1ff")
    crimeTypelbl.grid(row=5, column=2, sticky=W, padx=5, pady=10)
    crimeTypeEntry = Entry(criminalPanel,
                           font=("Times New Roman", 15))
    crimeTypeEntry.grid(row=5, column=3)

    # Committed crime entry and label
    committedCrimelbl = Label(criminalPanel,
                              text="Committed Crimes",
                              font=("Times New Roman", 15),
                              background="#b3d1ff")
    committedCrimelbl.grid(row=8, column=2, sticky=W, padx=5)
    committedCrimeEntry = Entry(criminalPanel,
                                font=("Times New Roman", 15))
    committedCrimeEntry.grid(row=8, column=3)

    # Birthmark label and entry
    birthMarklbl = Label(criminalPanel,
                         text="Birthmark",
                         font=("Times New Roman", 15),
                         background="#b3d1ff")
    birthMarklbl.grid(row=6, column=0, sticky=W, padx=5)
    birthMarkEntry = Entry(criminalPanel,
                           font=("Times New Roman", 15))
    birthMarkEntry.grid(row=6, column=1)

    # Contact
    contactnolbl = Label(criminalPanel,
                         text="Contact No",
                         font=("Times New Roman", 15),
                         background="#b3d1ff")
    contactnolbl.grid(row=6, column=2, sticky=W, padx=5)

    contactEntry = Entry(criminalPanel,
                         font=("Times New Roman", 15))
    contactEntry.grid(row=6, column=3)

    # Email label and entry
    emaillbl = Label(criminalPanel,
                     text="Email",
                     font=("Times New Roman", 15),
                     background="#b3d1ff")
    emaillbl.grid(row=9, column=0, sticky=W, padx=5)
    emailEntry = Entry(criminalPanel,
                       font=("Times New Roman", 15))
    emailEntry.grid(row=9, column=1, sticky=N, pady=10)

    # Function for clear
    def clear_text():
        caseIdEntry.delete(0, END)
        fatherEntry.delete(0, END)
        crmNameEntry.delete(0, END)
        nickNameEntry.delete(0, END)
        addressEntry.delete(0, END)
        crimeTypeEntry.delete(0, END)
        committedCrimeEntry.delete(0, END)
        birthMarkEntry.delete(0, END)
        contactEntry.delete(0, END)
        emailEntry.delete(0, END)
        display_img.configure(image='')

    def adddata(caseId, dob, criminalName, age, nickName, crimeDate, address, crimeType, birthMark, contactNo,
                fatherName, gender, mwanted, committedCrime, email):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='criminalmanagement',
                                                 user='root',
                                                 password='Levi@8355')
            if connection.is_connected():
                cursor = connection.cursor()
                queryTofetchFile = "select * from upload_image"
                cursor.execute(queryTofetchFile)
                fileRecords = cursor.fetchall()
                lastRecords = list(fileRecords[-1])
                queryToInsertData = f"Insert into criminalrecord values('{caseId}','{dob}','{criminalName}','{age}','{nickName}','{crimeDate}','{address}','{crimeType}','{birthMark}','{contactNo}','{fatherName}','{gender}','{mwanted}','{committedCrime}','{email}','{lastRecords[0]}')"
                cursor.execute(queryToInsertData)
                connection.commit()
                print(cursor.rowcount, "Records inserted successfully.")
                cursor.close()
                messagebox.showinfo("Success", "Data Inserted Successfully")
                clear_text()
        except Error as error:
            print("Failed to insert record into criminal record table{}".format(error))
        finally:
            if (connection.is_connected):
                connection.close()

    file_path = ""

    def open_img():
        global file_path
        selected_img = filedialog.askopenfile(title='open', initialdir="C:/")

        img = Image.open(selected_img.name)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        display_img.configure(image=img)
        display_img.image = img
        file_path = selected_img.name
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='criminalmanagement',
                                                 user="root",
                                                 password='Levi@8355')
            if connection.is_connected():
                cursor = connection.cursor()
                queryToInsert = f"insert into upload_image values('{file_path}')"
                cursor.execute(queryToInsert)
                connection.commit()
                cursor.close()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", "failed to upload image")
        finally:
            if connection.is_connected():
                connection.close()

                # validate page entered fields

    def validatePageFields(caseId, dob, criminalName, age, nickName, crimeDate, address, crimeType, birthMark,
                           contactNo, fatherName, gender, mwanted, committedCrime, email):
        print("dob " + dob)
        dob_date = datetime.strptime(dob, '%d-%m-%Y')
        cur_date = datetime.now()
        year1 = cur_date.year
        year2 = dob_date.year
        derAge = str(int(year1) - int(year2))
        age.configure(text=f"{derAge}")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        valid_mail = re.fullmatch(regex, email)
        valid_contact = contactNo.isdigit()
        valid_caseid = caseId.isdigit()

        # print("valid or not "+valid_mail)
        if (
                caseId == '' or dob == '' or criminalName == '' or nickName == '' or crimeDate == '' or address == '' or crimeType == '' or birthMark == '' or contactNo == '' or fatherName == '' or committedCrime == '' or email == ''):
            messagebox.showerror("Error", "Each and every field is mandatory.")
            return 0
        elif (valid_mail == None):
            messagebox.showerror("Error", "Invalid Email Entered")
            return 0
        elif (len(contactNo) != 10):
            messagebox.showerror("Error", "Contact number must be 10 digits")
            return 0
        elif (valid_contact == False):
            messagebox.showerror("Error", "Contact number number must be numbered value")
            return 0
        elif (valid_caseid == False):
            messagebox.showerror("Error", "Case id must be integer value")
            return 0
        adddata(caseId, dob, criminalName, derAge, nickName, crimeDate, address, crimeType, birthMark, contactNo,
                fatherName, gender, mwanted, committedCrime, email)

    # Buttons save,clear,modify, view
    modifybtn = Button(criminalPanel,
                       text="Modify",
                       font=("Times New Roman", 15),
                       command=lambda: modificationPage(username, inchargename))
    modifybtn.grid(row=11, column=2, pady=10)
    clearbtn = Button(criminalPanel,
                      text="clear",
                      font=("Times New Roman", 15))
    clearbtn.grid(row=11, column=3, pady=10)
    viewbtn = Button(criminalPanel,
                     text="View",
                     font=("Times New Roman", 15),
                     command=displayRecord)
    viewbtn.grid(row=11, column=4, pady=10)

    # photo frame for criminal
    photoFrame = Frame(criminalPanel,
                       highlightbackground="black",
                       # highlightthickness=3,
                       width=300,
                       height=300)

    photoFrame.grid(row=2, column=5, rowspan=6, columnspan=2, sticky=N)
    display_img = Label(photoFrame)
    display_img.grid(row=0, column=0)

    photobtn = Button(criminalPanel,
                      text="select image",
                      command=open_img,
                      font=("Times New Roman", 15))
    photobtn.grid(row=9, column=4, columnspan=3, sticky=N)
    savebtn = Button(criminalPanel,
                     text="Save",
                     font=("Times New Roman", 15),
                     command=lambda: validatePageFields(caseIdEntry.get(), dobpicker.get(), crmNameEntry.get(),
                                                        derAgeLbl, nickNameEntry.get(), crimedatePicker.get(),
                                                        addressEntry.get(), crimeTypeEntry.get(), birthMarkEntry.get(),
                                                        contactEntry.get(), fatherEntry.get(), gendervar.get(),
                                                        mwantedvar.get(), committedCrimeEntry.get(), emailEntry.get()))
    savebtn.grid(row=11, column=1, pady=10)
    clearbtn.configure(command=clear_text)


def modificationPage(username, inchargename):
    modifiedPanel = Toplevel(criminalPanel, background="#b3d1ff")
    w, h = modifiedPanel.winfo_screenwidth(), modifiedPanel.winfo_screenheight()
    modifiedPanel.geometry("%dx%d+0+0" % (w, h))
    modifiedPanel.configure(background="#b3d1ff")
    modifiedPanel.state('zoomed')
    modifiedPanel.title("Modification Panel")
    # Modify page title
    modifyTitlelbl = Label(modifiedPanel,
                           text="Modification Page",
                           font=("Times New Roman", 25),
                           background="#b3d1ff")
    modifyTitlelbl.grid(row=0, column=3, columnspan=2)

    # Incharge Name and label
    inchUsername = Label(modifiedPanel,
                         text=f"Username: {username}",
                         font=("Times New Roman", 15),
                         background="#b3d1ff")
    inchUsername.grid(row=1, column=0, padx=5, pady=10)

    inchName = Label(modifiedPanel,
                     text=f"Incharge name: {inchargename}",
                     font=("Times New Roman", 15),
                     background="#b3d1ff")
    inchName.grid(row=1, column=5, padx=5, pady=10)

    # case id label dropdown
    caseIdlbl = Label(modifiedPanel,
                      text="Case Id",
                      font=("Times New Roman", 15),
                      background="#b3d1ff")
    caseIdlbl.grid(row=2, column=0, sticky=W, padx=5)
    caseIdlist1 = []
    try:
        connection = mysql.connector.connect(host="localhost",
                                             database='criminalmanagement',
                                             user='root',
                                             password='Levi@8355')
        if connection.is_connected():
            cursor = connection.cursor()
            queryTofetchCaseId = "select caseId from criminalrecord;"
            cursor.execute(queryTofetchCaseId)
            allcaseId = cursor.fetchall()
            for item in allcaseId:
                for each in item:
                    caseIdlist1.append(each)
            # print(caseIdlist1)
    except Error as error:
        messagebox.showinfo("Error", f"{error}")
    finally:
        if connection.is_connected():
            connection.close()

    # DOB entry and labels
    doblbl = Label(modifiedPanel,
                   text="DOB",
                   font=("Times New Roman", 15),
                   background="#b3d1ff")
    doblbl.grid(row=2, column=2, sticky=W, padx=5)
    dobpicker = DateEntry(modifiedPanel, year=2019, month=6, day=22,
                          background='darkblue', foreground='white', borderwidth=2,
                          date_pattern='dd-mm-yyyy')
    dobpicker.grid(row=2, column=3, sticky=W)

    # father label and entry
    fatherlbl = Label(modifiedPanel,
                      text="Father Name",
                      font=("Times New Roman", 15),
                      background="#b3d1ff")
    fatherlbl.grid(row=7, column=0, sticky=W, padx=5)
    fatherEntry = Entry(modifiedPanel,
                        font=("Times New Roman", 15))
    fatherEntry.grid(row=7, column=1)

    # CriminalName entry and labels
    crmNamelbl = Label(modifiedPanel,
                       text="Criminal Name",
                       font=("Times New Roman", 15),
                       background="#b3d1ff")
    crmNamelbl.grid(row=3, column=0, sticky=W, padx=5, pady=10)
    crmNameEntry = Entry(modifiedPanel,
                         font=("Times New Roman", 15))
    crmNameEntry.grid(row=3, column=1)

    ageLbl = Label(modifiedPanel,
                   text="Age",
                   font=("Times New Roman", 15),
                   background="#b3d1ff")
    ageLbl.grid(row=3, column=2, sticky=W, padx=5, pady=10)
    derAgeLbl = Label(modifiedPanel,
                      text="Derived",
                      font=("Times New Roman", 15),
                      background="#b3d1ff")
    derAgeLbl.grid(row=3, column=3, sticky=W)

    # Gender label and radiobutton
    genderlbl = Label(modifiedPanel,
                      text="Gender",
                      font=("Times New Roman", 15),
                      background="#b3d1ff")
    genderlbl.grid(row=7, column=2, sticky=W, padx=5, pady=10)
    genderFrame = Frame(modifiedPanel,
                        background="#b3d1ff")
    genderFrame.grid(row=7, column=3, columnspan=3, sticky=W)

    gendervar = StringVar()
    maleradiobtn = Radiobutton(genderFrame,
                               text="Male",
                               variable=gendervar,
                               value="male")
    maleradiobtn.grid(row=0, column=0, sticky=W)
    femaleradiobtn = Radiobutton(genderFrame,
                                 text="Female",
                                 variable=gendervar,
                                 value="female")
    femaleradiobtn.grid(row=0, column=1, sticky=W)

    # nick name label and entry
    nickNamelbl = Label(modifiedPanel,
                        text="Nick Name",
                        font=("Times New Roman", 15),
                        background="#b3d1ff")
    nickNamelbl.grid(row=4, column=0, sticky=W, padx=5)
    nickNameEntry = Entry(modifiedPanel,
                          font=("Times New Roman", 15))
    nickNameEntry.grid(row=4, column=1)

    # Crime date and its label
    crimedatelbl = Label(modifiedPanel,
                         text="Crime Date",
                         font=("Times New Roman", 15),
                         background="#b3d1ff")
    crimedatelbl.grid(row=4, column=2, sticky=W, padx=5)
    crimedatePicker = DateEntry(modifiedPanel, day=22, month=6, year=2019,
                                background='darkblue', foreground='white', borderwidth=2,
                                date_pattern='dd-mm-yyyy')
    crimedatePicker.grid(row=4, column=3, sticky=W)

    # Most wanted label and frame
    mwantedlbl = Label(modifiedPanel,
                       text="Most Wanted",
                       font=("Times New Roman", 15),
                       background="#b3d1ff")
    mwantedlbl.grid(row=8, column=0, sticky=W, padx=5)

    mwantedFrame = Frame(modifiedPanel)
    mwantedFrame.grid(row=8, column=1, sticky=W)
    mwantedvar = StringVar()

    yesradiobtn = Radiobutton(mwantedFrame,
                              text="Yes",
                              variable=mwantedvar,
                              value="yes")
    yesradiobtn.grid(row=0, column=0)
    noradiobtn = Radiobutton(mwantedFrame,
                             text="No",
                             variable=mwantedvar,
                             value="no")
    noradiobtn.grid(row=0, column=1)

    # Address fields
    addresslbl = Label(modifiedPanel,
                       text="Adress",
                       font=("Times New Roman", 15),
                       background="#b3d1ff")
    addresslbl.grid(row=5, column=0, sticky=W, padx=5, pady=10)
    addressEntry = Entry(modifiedPanel,
                         font=("Times New Roman", 15))
    addressEntry.grid(row=5, column=1)

    # Crime type label and entry
    crimeTypelbl = Label(modifiedPanel,
                         text="Crime Type",
                         font=("Times New Roman", 15),
                         background="#b3d1ff")
    crimeTypelbl.grid(row=5, column=2, sticky=W, padx=5, pady=10)
    crimeTypeEntry = Entry(modifiedPanel,
                           font=("Times New Roman", 15))
    crimeTypeEntry.grid(row=5, column=3)

    # Committed crime entry and label
    committedCrimelbl = Label(modifiedPanel,
                              text="Committed Crimes",
                              font=("Times New Roman", 15),
                              background="#b3d1ff")
    committedCrimelbl.grid(row=8, column=2, sticky=W, padx=5)
    committedCrimeEntry = Entry(modifiedPanel,
                                font=("Times New Roman", 15))
    committedCrimeEntry.grid(row=8, column=3)

    # Birthmark label and entry
    birthMarklbl = Label(modifiedPanel,
                         text="Birthmark",
                         font=("Times New Roman", 15),
                         background="#b3d1ff")
    birthMarklbl.grid(row=6, column=0, sticky=W, padx=5)
    birthMarkEntry = Entry(modifiedPanel,
                           font=("Times New Roman", 15))
    birthMarkEntry.grid(row=6, column=1)

    # Contact
    contactnolbl = Label(modifiedPanel,
                         text="Contact No",
                         font=("Times New Roman", 15),
                         background="#b3d1ff")
    contactnolbl.grid(row=6, column=2, sticky=W, padx=5)

    contactEntry = Entry(modifiedPanel,
                         font=("Times New Roman", 15))
    contactEntry.grid(row=6, column=3)

    # Email label and entry
    emaillbl = Label(modifiedPanel,
                     text="Email",
                     font=("Times New Roman", 15),
                     background="#b3d1ff")
    emaillbl.grid(row=9, column=0, sticky=W, padx=5)
    emailEntry = Entry(modifiedPanel,
                       font=("Times New Roman", 15))
    emailEntry.grid(row=9, column=1, sticky=N, pady=10)

    # photo frame for criminal
    photoFrame = Frame(modifiedPanel,
                       highlightbackground="black",
                       width=300,
                       height=300)
    photoFrame.grid(row=2, column=5, rowspan=6, columnspan=2, sticky=N)
    display_img = Label(photoFrame)
    display_img.grid(row=0, column=0)

    def fillCriminalDetail(events):
        clear_text()
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='criminalmanagement',
                                                 user='root',
                                                 password='Levi@8355')
            queryToFetchData = f"select * from criminalrecord where caseId={clicked.get()}"
            cursor = connection.cursor()
            cursor.execute(queryToFetchData)
            allrecords = cursor.fetchall()
            allrecords = list(allrecords[0])
            print(allrecords)
            # dobpicker.configure
            print(dobpicker)
            dobpicker.insert(0, allrecords[1])
            crmNameEntry.insert(0, allrecords[2])
            derAgeLbl.configure(text=f"{allrecords[3]}")
            nickNameEntry.insert(0, allrecords[4])
            crimedatePicker.insert(0, allrecords[5])
            addressEntry.insert(0, allrecords[6])
            crimeTypeEntry.insert(0, allrecords[7])
            birthMarkEntry.insert(0, allrecords[8])
            contactEntry.insert(0, allrecords[9])
            fatherEntry.insert(0, allrecords[10])
            gendervar.set(allrecords[11])
            mwantedvar.set(allrecords[12])
            committedCrimeEntry.insert(0, allrecords[13])
            emailEntry.insert(0, allrecords[14])
            img_path = Image.open(f'{allrecords[15]}')
            img_path = img_path.resize((250, 250), Image.ANTIALIAS)
            img_path = ImageTk.PhotoImage(img_path)
            display_img.configure(image=img_path)
            display_img.image = img_path
        except:
            print("you have selected ", clicked.get())
        finally:
            if connection.is_connected():
                connection.close()

                # openImg function

    def open_img(case_id):
        global file_path
        display_img.configure(image='')
        selected_img = filedialog.askopenfile(title='open', initialdir="C:/")
        img = Image.open(selected_img.name)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        display_img.configure(image=img)
        display_img.image = img
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='criminalmanagement',
                                                 user='root',
                                                 password='Levi@8355')
            queryToDeletePic = f"update criminalrecord set photopath='{selected_img.name}' where caseId = '{case_id}'"
            cursor = connection.cursor()
            cursor.execute(queryToDeletePic)
            connection.commit()
            messagebox.showinfo("Success", "Picture updated successfully!")
        except Error as error:
            print("Modified pic can't be inserted ", error)
        finally:
            if (connection.is_connected):
                connection.close()

    # Function for clear
    def clear_text():
        fatherEntry.delete(0, END)
        crmNameEntry.delete(0, END)
        nickNameEntry.delete(0, END)
        addressEntry.delete(0, END)
        crimeTypeEntry.delete(0, END)
        committedCrimeEntry.delete(0, END)
        birthMarkEntry.delete(0, END)
        contactEntry.delete(0, END)
        emailEntry.delete(0, END)
        dobpicker.delete(0, END)
        crimedatePicker.delete(0, END)
        display_img.configure(image="")

    def updateRecord(caseId, dob, criminalName, derAge, nickname, crimeDate, address, crimeType, birthmark, contactNo,
                     fatherName, gender, mWanted, committedCrime, email):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='criminalmanagement',
                                                 user='root',
                                                 password='Levi@8355')
            if (connection.is_connected):
                queryForUpdate = f"""update criminalrecord 
                                    set dob = '{dob}',criminalName = '{criminalName}',age = '{derAge}',nickName='{nickname}',crimeDate='{crimeDate}',address='{address}',crimeType='{crimeType}',birthMark='{birthmark}',contactNo='{contactNo}',fatherName='{fatherName}',gender='{gender}',mWanted='{mWanted}',committedCrimes='{committedCrime}',email='{email}'
                                    where caseId = '{caseId}'"""
                cursor = connection.cursor()
                cursor.execute(queryForUpdate)
                connection.commit()
                messagebox.showinfo("Success", "Data updated successfully!")
        except Error as error:
            print("Failed to update table ", error)
        finally:
            if (connection.is_connected):
                connection.close()

    def validatePage(caseId, dob, criminalName, age, nickName, crimeDate, address, crimeType, birthMark, contactNo,
                     fatherName, gender, mwanted, committedCrime, email):
        print("dob " + dob)
        dob_date = datetime.strptime(dob, '%d-%m-%Y')
        cur_date = datetime.now()
        year1 = cur_date.year
        year2 = dob_date.year
        derAge = str(int(year1) - int(year2))
        age.configure(text=f"{derAge}")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        valid_mail = re.fullmatch(regex, email)
        valid_contact = contactNo.isdigit()
        # print("valid or not "+valid_mail)

        if (
                caseId == '' or dob == '' or criminalName == '' or nickName == '' or crimeDate == '' or address == '' or crimeType == '' or birthMark == '' or contactNo == '' or fatherName == '' or committedCrime == '' or email == ''):
            messagebox.showerror("Error", "Each and every field is mandatory.")
            return 0
        elif (valid_mail == None):
            messagebox.showerror("Error", "Invalid Email Entered")
            return 0
        elif (len(contactNo) != 10):
            messagebox.showerror("Error", "Contact number must be 10 digits")
            return 0
        elif (valid_contact == False):
            messagebox.showerror("Error", "Contact number number must be numbered value")
            return 0
        updateRecord(caseId, dob, criminalName, derAge, nickName, crimeDate, address, crimeType, birthMark, contactNo,
                     fatherName, gender, mwanted, committedCrime, email)

    # deleting data from database
    def deleteData(caseId):
        print("caseid is ", caseId)
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='criminalmanagement',
                                                 user='root',
                                                 password='Levi@8355')
            queryToFetchData = f"select * from criminalrecord where caseId = '{caseId}'"
            cursor = connection.cursor()
            cursor.execute(queryToFetchData)
            records = cursor.fetchall()
            records = list(records[0])
            deletequery = f"delete from criminalrecord where caseId = '{caseId}'"
            cursor.execute(deletequery)
            connection.commit()
            messagebox.showinfo("Success", "Data deleted successfully")
            clear_text()
        except Error as error:
            print("Error reading from mysql", error)
            messagebox.showerror("Error", "Data cannot be deleted.")
        finally:
            if (connection.is_connected):
                connection.close()

    # Buttons save,clear,modify, view
    clicked = StringVar()
    clicked.set("Select CaseId")
    dropdownCaseid = OptionMenu(modifiedPanel, clicked, *caseIdlist1, command=fillCriminalDetail)
    dropdownCaseid.grid(row=2, column=1, sticky=W)

    updatebtn = Button(modifiedPanel,
                       text="Update",
                       font=("Times New Roman", 15),
                       command=lambda: validatePage(clicked.get(), dobpicker.get(), crmNameEntry.get(), derAgeLbl,
                                                    nickNameEntry.get(), crimedatePicker.get(), addressEntry.get(),
                                                    crimeTypeEntry.get(), birthMarkEntry.get(), contactEntry.get(),
                                                    fatherEntry.get(), gendervar.get(), mwantedvar.get(),
                                                    committedCrimeEntry.get(), emailEntry.get()))
    updatebtn.grid(row=11, column=1, pady=10)

    deletebtn = Button(modifiedPanel,
                       text="Delete",
                       font=("Times New Roman", 15),
                       command=lambda: deleteData(clicked.get()))
    deletebtn.grid(row=11, column=2, pady=10)

    photobtn = Button(modifiedPanel,
                      text="select image",
                      command=lambda: open_img(clicked.get()),
                      font=("Times New Roman", 15))
    photobtn.grid(row=9, column=4, columnspan=3, sticky=N)

    clearbtn = Button(modifiedPanel,
                      text="clear",
                      font=("Times New Roman", 15))
    clearbtn.grid(row=11, column=3, pady=10)
    clearbtn.configure(command=clear_text)
    exitbtn = Button(modifiedPanel,
                     text="Exit",
                     font=("Times New Roman", 15),
                     command=lambda: modifiedPanel.destroy())
    exitbtn.grid(row=11, column=4, pady=10)


def displayRecord():
    displayPanel = Toplevel(criminalPanel, background="#b3d1ff")
    w, h = displayPanel.winfo_screenwidth(), displayPanel.winfo_screenheight()
    displayPanel.geometry("%dx%d+0+0" % (w, h))
    displayPanel.title("Display Records")
    displayPanel.state('zoom')
    # Title and label
    # distLbl = Label(displayPanel,
    #                 text="Criminal Records",
    #                 font=("Times New Roman",25),
    #                 background="#b3d1ff")
    # distLbl.grid(row=0,column=0, sticky='nsew')
    tv = ttk.Treeview(displayPanel,
                      columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                      show="headings",
                      selectmode='browse',
                      height=700)

    tv.grid(row=0, column=0)
    tv.heading(1, text="Case id")
    tv.column(1, width=85)
    tv.heading(2, text="DOB")
    tv.column(2, width=85)
    tv.heading(3, text="Criminal Name")
    tv.column(3, width=85)
    tv.heading(4, text="Age")
    tv.column(4, width=85)
    tv.heading(5, text="Nick Name")
    tv.column(5, width=85)
    tv.heading(6, text="Crime Date")
    tv.column(6, width=85)
    tv.heading(7, text="Address")
    tv.column(7, width=85)
    tv.heading(8, text="Crime Type")
    tv.column(8, width=85)
    tv.heading(9, text="Birth Mark")
    tv.column(9, width=85)
    tv.heading(10, text="Contact No")
    tv.column(10, width=85)
    tv.heading(11, text="Father Name")
    tv.column(11, width=85)
    tv.heading(12, text="Gender")
    tv.column(12, width=85)
    tv.heading(13, text="Most Wanted")
    tv.column(13, width=85)
    tv.heading(14, text="Committed Crimes")
    tv.column(14, width=85)
    tv.heading(15, text="Email")
    tv.column(15, width=85)
    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='criminalmanagement',
                                             user='root',
                                             password='Levi@8355')
        queryToGetAllrecord = f"select * from criminalrecord;"
        cursor = connection.cursor()
        cursor.execute(queryToGetAllrecord)
        allRecords = cursor.fetchall()
        print(allRecords)
    except Error as error:
        print("cannot fetch the data ", error)
    finally:
        if (connection.is_connected):
            connection.close()

    for detail in allRecords:
        tv.insert('', END, values=detail)


loginpagePanel()