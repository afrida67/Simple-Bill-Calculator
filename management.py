from tkinter import *
from PIL import ImageTk, Image
import random
import time
import datetime

root = Tk()
root.geometry("1600x700+0+0")
root.title("Harry Potter Restaurant")

Tops = Frame(root,width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

####################### Time ####################

localtime=time.asctime(time.localtime(time.time()))

#################### Top ####################
toptitle = Label(Tops,font=('helvetica',30,'bold'),text="Harry Potter Restaurant ",fg="Black",bd=10,anchor='w')
toptitle.grid(row=0,column=0)

timeS = Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
timeS.grid(row=1,column=0)

root.mainloop()