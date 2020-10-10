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
	send = Button(root,text="Send",padx=30,bg="orange",relief=RIDGE,borderwidth=1,font=('veranda',10,'bold'),cursor="hand2",command=send)
	send.place(x=350,y=360)
	root.mainloop( )
	except:
		messagebox.showerror('Login Error',"Failed to login, either your email or password is wrong.")
		
		
def logout( ):
			s.quit( )
			root.destroy( )
			header1=Label(root,bg="orange",width =300,height=2)
			header1.place(x=0,y=0)
			h2=Label(root,text="Email Sender",bg="orange",fg="black",font=('veranda',13,'bold'))
			h2.place(x=175,y=5)
			logout=Button(root,text="Log Out",padx=20,bg="orange",relief=RIDGE,borderwidth=1,font=('veranda',10,'bold'),cursor="hand2",command=logout)
			logout.place(x=390,y=38)
			r=Label(root,text="Recipetent Email Address",font('veranda',10,'bold'))
			r.place(x=130,y=130)
			recipetent=Entry(root,width=30,relief=RIDGE,borderwidth=3)
			recipetent.place(x=130,y=150)
			sub=Label(root,text="Subject",font=('veranda',10,'bold'))
			sub.place(x=130,y=190)
			subject=Entry(root,width=30,relief=RIDGE,borderwidth=3)
			subject.place(x=130,y=210)
			m=Label(root,text="Message",font=('veranda',10,'bold'))
			m.place(x=130,y=250)
			message=ScrolledText(root,width=40,height=5,relief=RIDGE,borderwidth=3)
			message.place(x=130,y=270)
			
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

# closing the GUI
root.mainloop( )