from tkinter import*
from PIL import ImageTk, Image
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.resizable(width=True, height=True)
root.title("HP Restaurant")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#==============================Time======================================#
localtime = time.asctime(time.localtime(time.time()))

titleInfo = Label(Tops,font=('helvetica',30,'bold'),text="Harry Potter Restaurant",fg="Black",bd=10,anchor='w')
titleInfo.grid(row=0,column=0)

timeInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
timeInfo.grid(row=1,column=0)

#===================================dropdown==============================================# 
variable = StringVar(root)
variable.set("Menu") # default value

w = OptionMenu(root, variable, "Menu", "Price List")
w.pack()

#===================================declarations==============================================# 
rand = StringVar()
pasta = StringVar()
noodles = StringVar()
soup = StringVar()
drinks = StringVar()
burger = StringVar()
subTotal = StringVar()
total = StringVar()
vat = StringVar()
cost = StringVar()

def count():
    x=random.randint(10,50)
    randomRef=str(x)
    rand.set(randomRef)

    if (pasta.get()== ""):
        pastaCost = 0
    else:
        pastaCost  = float(pasta.get())

    if (noodles.get()==""):
        noodlesCost = 0
    else:
        noodlesCost = float(noodles.get())

    if (soup.get() == ""):
        soupCost = 0
    else:
        soupCost = float(soup.get())

    if (burger.get() == ""):
        burgerCost = 0
    else:
        burgerCost = float(burger.get())
     
    if (drinks.get() == ""):
        drinksCost = 0
    else:
        drinksCost = float(drinks.get())
                
    costOfPasta = pastaCost * 10
    costOfDrinks = drinksCost * 10
    costOfNoodles = noodlesCost * 10
    costOfSoup = soupCost * 10
    costOfBurger = burgerCost * 10


    CostofMeal = "Rs", str ('%.2f' % (costOfPasta + costOfDrinks + costOfNoodles + costOfSoup + costOfBurger))

    payVat = ((costOfPasta + costOfDrinks + costOfNoodles + costOfSoup + costOfBurger) * 0.15)

    TotalCost = (costOfPasta + costOfDrinks + costOfNoodles + costOfSoup + costOfBurger)

    OverAllCost = "Rs", str ('%.2f' % (payVat + TotalCost))

    paidVat = "Rs", str ('%.2f' % payVat)

    cost.set(CostofMeal)
    vat.set(paidVat)
    subTotal.set(CostofMeal)
    total.set(OverAllCost)
    
def qExit():
    root.destroy()

def reset():
    rand.set("") 
    pasta.set("")
    burger.set("")
    noodles.set("")
    drinks.set("")
    soup.set("")
    subTotal.set("")
    vat.set("")
    cost.set("")
    total.set("")
 

#===================================Menu List===================================#

pastaLabel = Label(f1, font=('arial', 16, 'bold'),text="Pasta", bd=16,anchor="w")
pastaLabel.grid(row=1, column=0)
bxPasta = Entry(f1, font=('arial',16,'bold'),textvariable = pasta, bd=10, insertwidth=4,bg="powder blue",justify='right')
bxPasta.grid(row=1,column=1)


noodlesLabel = Label(f1, font=('arial', 16, 'bold'),text="Chowmein",bd=16,anchor="w")
noodlesLabel.grid(row=2, column=0)
bxNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=noodles,bd=10,insertwidth=4,bg="powder blue",justify='right')
bxNoodles.grid(row=2,column=1)


soupLabel = Label(f1, font=('arial', 16, 'bold'),text="Soup",bd=16,anchor="w")
soupLabel.grid(row=3, column=0)
bxSoup=Entry(f1, font=('arial',16,'bold'),textvariable=soup,bd=10,insertwidth=4,bg="powder blue",justify='right')
bxSoup.grid(row=3,column=1)

burgerLabel = Label(f1, font=('arial', 16, 'bold'),text="Burger",bd=16,anchor="w")
burgerLabel.grid(row=4, column=0)
bxBurger=Entry(f1, font=('arial',16,'bold'),textvariable=burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
bxBurger.grid(row=4,column=1)

drinksLabel = Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
drinksLabel.grid(row=5, column=0)
bxDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
bxDrinks.grid(row=5,column=1)

#===================================Total Price===================================#


orderLabel = Label(f1, font=('arial', 16, 'bold'),text="Order No",bd=16,anchor="w")
orderLabel.grid(row=1, column=2)
bxOrder = Entry(f1, font=('arial',16,'bold'),textvariable=rand, bd=10, insertwidth=4, bg="powder blue",justify='right')
bxOrder.grid(row=1,column=3)

costLabel = Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
costLabel.grid(row=2, column=2)
bxCost=Entry(f1, font=('arial',16,'bold'),textvariable=cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
bxCost.grid(row=2,column=3)


vatLabel = Label(f1, font=('arial', 16, 'bold'),text="15% Vat",bd=16,anchor="w")
vatLabel.grid(row=3, column=2)
bxVat = Entry(f1, font=('arial',16,'bold'),textvariable=vat,bd=10,insertwidth=4,bg="powder blue",justify='right')
bxVat.grid(row=3,column=3)

subTotalLabel = Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
subTotalLabel.grid(row=4, column=2)
bxSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=subTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
bxSubTotal.grid(row=4,column=3)

totalCostLabel = Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
totalCostLabel.grid(row=5, column=2)
bxTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=total,bd=10,insertwidth=4,bg="powder blue",justify='right')
bxTotalCost.grid(row=5,column=3)

#menu#
lblTest= Label(f1, font=('arial', 16, 'bold'),text="burger",bd=16,anchor="w")
lblTest.grid(row=5, column=4)

#==========================================Buttons================================#
btnTotal = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=count).grid(row=7,column=1)

btnReset = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=reset).grid(row=7,column=2)

btnExit = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)


'''imgpath = 'd.png'
img = PhotoImage(file=imgpath)
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")'''

root.mainloop()


