import tkinter as t
import string
from tkinter import ttk
from tkinter import *
import random
import pyperclip

window=t.Tk()

choice=IntVar()

def generate():
    e.delete(0,"end")
    small=string.ascii_lowercase
    capital=string.ascii_uppercase
    numbers=string.digits
    special=string.punctuation
    all=small+capital+numbers+special

    password_length=int(lb.get())
    password=random.sample(all,password_length)

    if choice.get()==1:
        e.insert(0,random.sample(small+capital,password_length))

    if choice.get()==2:
        e.insert(0,random.sample(small+capital+numbers,password_length))

    if choice.get()==3:
        e.insert(0,random.sample(all,password_length))

def copy():
    password=e.get()
    pyperclip.copy(password)



window.title("password generator")
window.config(bg='#17161b')
l1=t.Label(window,text="Password Generator",fg="#fff",bg="#17161b",font=("arial",20))
l1.grid(pady=8)
r1=t.Radiobutton(window,text="Weak",value=1,variable=choice,font=("arial",15,'bold'))
r1.grid(pady=8)
r2=t.Radiobutton(window,text="Medium",value=2,variable=choice,font=("arial",15,'bold'))
r2.grid(pady=8)
r3=t.Radiobutton(window,text="Strong",value=3,variable=choice,font=("arial",15,'bold'))
r3.grid(pady=8)

l2=t.Label(window,text="Password Length",fg="#fff",bg="#17161b",font=("arial",15))
l2.grid(pady=8)

lb=t.Spinbox(window,width=5,from_=6,to_=18,fg="#17161b",bg="#fff",font=("arial",15,'bold'))
lb.grid()

b1=t.Button(window,text="Generate",bd=1,fg="#fff",bg="#3697f5",font=("arial",15),command=generate)
b1.grid(pady=15)



e=t.Entry(window,width=30,bd=2)
e.grid(pady=20)



b2=t.Button(window,text="Copy",bd=1,fg="#fff",bg="#3697f5",font=("arial",15),command=copy)
b2.grid(pady=8)

window.mainloop()