from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import DataBase

jan = Tk()
jan.title("DP Systems - Access Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/logoIcon.ico")
logo = PhotoImage(file="icons/logo.png")

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE", relief="raise")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", relief="raise")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Password", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", relief="raise")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

def Login():
    User = UserEntry.get()
    Password = PassEntry.get()
    DataBase.cur.execute('''
    SELECT User, Password FROM Users
    WHERE User=? AND Password=?                     
    ''', (User, Password))
    VerifyLogin = DataBase.cur.fetchone()
    try:
        if (User in VerifyLogin or Password in VerifyLogin):
            messagebox.showinfo("Success","Logou!")
    except:
        messagebox.showerror("Error", "Por favor, verifique seu usuário ou senha!")

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register(RegisterButton):
    LoginButton.place_forget()
    RegisterButton.place_forget()

    NomeLabel = Label(RightFrame, text="Name", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=37)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=37)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Password = PassEntry.get()

        if Name == "" or Email == "":
            messagebox.showerror("Error", "Por favor, preencha todos os campos")
        else:
            DataBase.cur.execute('''
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            ''', (Name, Email, User, Password))
            DataBase.conn.commit()
            DataBase.conn.close()
            messagebox.showinfo("Success", "Registrado com sucesso!")

    RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=RegisterToDataBase)
    RegisterButton.place(x=100, y=225)

    def BackToLogin():
        NomeLabel.place_forget()
        NomeEntry.place_forget()
        EmailLabel.place_forget()
        EmailEntry.place_forget()
        RegisterButton.place_forget()
        BackButton.place_forget()

        LoginButton.place(x=100, y=225)
        RegisterButton.place(x=125, y=260)

    BackButton = ttk.Button(RightFrame, text="Back", width=20, command=lambda: BackToLogin())
    BackButton.place(x=125, y=260)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=lambda: Register(RegisterButton))
RegisterButton.place(x=125, y=260)

jan.mainloop()
