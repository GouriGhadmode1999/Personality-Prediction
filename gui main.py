# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""

from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
from pymsgbox import *


root=tk.Tk()

root.title("personality_Prediction")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

bg = Image.open(r"E:/personality_Prediction/bg1.jpg")
bg.resize((1800,800),Image.ANTIALIAS)
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=93)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="personality_Prediction",width=40,background="#00BFFF",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=15)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#00BFFF")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login1.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


wlcm=tk.Label(root,text="......Welcome to personality_Prediction System ......",width=90,height=3,background="#00BFFF",foreground="black",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=620)




d2=tk.Button(root,text="Login",command=Login,width=9,height=2,bd=0,background="#00BFFF",foreground="black",font=("times new roman",14,"bold"))
d2.place(x=1000,y=18)


d3=tk.Button(root,text="Register",command=Register,width=9,height=2,bd=0,background="#00BFFF",foreground="black",font=("times new roman",14,"bold"))
d3.place(x=1100,y=18)



root.mainloop()
