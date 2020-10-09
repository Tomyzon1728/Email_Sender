# importing necessary modules
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
#import smptlib
from tkinter.scrolledtext import ScrolledText

# creating the foundation of the graphical user interface whilst giving appropriate title and reshaping to taste.
root=tk.Tk( )
root.title("fastrack\nEmail Sender")
root.geometry("400x300")
root.maxsize(400,300)
root.minsize(400,300)

def Login():
    pass

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
email=Entry(root,width=30,relief=RIDGE,borderwidth=3)
email.place(x=100,y=150)
p=Label(root,text="Password",font=('veranda',10,'bold'))
p.place(x=100,y=190)
password=Entry(root,width=30,relief=RIDGE,borderwidth=3)
password.place(x=100,y=210)
login=Button(root,text="Log in",padx=30,bg="orange",relief=RIDGE,borderwidth=1,font=('veranda',10,'bold'),cursor="hand2",command=Login)
login.place(x=135,y=240)

# closing the GUI
root.mainloop( )