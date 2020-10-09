# importing necessary modules
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import smptlib
from tkinter.scrolledtext import ScrolledText

# creating the foundation of the graphical user interface whilst giving appropriate title and reshaping to taste.
root=tk.Tk( )
root.title("fastrack\nEmail Sender")
root.geometry("400x300")
root.maxsize(400,300)
root.minsize(400,300)

# creating a login function which checks for validity of an email as well as empty str for password
def Login():
    e=email.get( )
    p=password.get( )
    if "@gmail.com" not in e or e== " ":
    	messagebox.showerror('Login error',"Please write a valid email")
    elif p== " ":
    	messagebox.showerror('Login error',"Password shouldn't be left empty")
    else:
    	try:
    		s= smtplib.SMTP( 'smtp.gmail.com',587)
    		s.starttls( )
    		s.login(e,p)
    		message.showinfo("Login success","You have logged to gmail successfully")
    		root=tk.Tk()
    		root.geometry("500x400")

def send( ):
	r=recipetent.get( )
	sub=subject.get( )
	m=message.get('1.0',END)
	if "@gmail.com" not in r or r==" ":
		messagebox.showerror("Sending mail error","write a valid Email")
	elif m ==" ":
		messagebox.showerror("Sending mail error","message shouldn't be empty")
	else:
		s.sendmail(r,e,f'subject :{sub}\n\n {m}')
		messagebox.showinfo("sucess","Your message has been sent sucessfully")
			
# creating header of the GUI
header= Label(root,bg="orange",width=300,height=2)
header.place(x=0,y=0)
h1=Label(root,text="Email Sender",bg="orange",fg="black",font=('veranda',13,'bold'))
h1.place(x=135,y=5)
load= Image.open('gmail.png')
img= ImageTk.PhotoImage(load, master =root)
logo=Label(root,image=img,borderwidth=0)
logo.place(x=150,y=38)
e=Label(root,text="Email Address",font=('veranda',10,'bold'))
e.place(x=100,y=130)

# creating an entry box for email and password
email=Entry(root,width=30,relief=RIDGE,borderwidth=3)
email.place(x=100,y=150)
p=Label(root,text="Password",font=('veranda',10,'bold'))
p.place(x=100,y=190)
password=Entry(root,width=30,relief=RIDGE,borderwidth=3)
password.place(x=100,y=210)

# creating login button
login=Button(root,text="Log in",padx=30,bg="orange",relief=RIDGE,borderwidth=1,font=('veranda',10,'bold'),cursor="hand2",command=Login)
login.place(x=135,y=240)

# creating send Button
send = Button(root,text="Send",padx=30,bg="orange",relief=RIDGE,borderwidth=1,font=('veranda',10,'bold'),cursor="hand2",command=send)
send.place(x=350,y=360)

# closing the GUI
root.mainloop( )