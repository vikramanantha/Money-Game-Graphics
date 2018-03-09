import tkinter as tk
from tkinter.ttk import *
import time
import random
score = 0
rate = 1
likenessLevel = 0
boughtItems = []
HiredItems = []
lossmoney = [0, 0.1, 0.25, 0.5, 0.2, 0.33, 0.75, 0.99]
winmoney = [1, 1.2, 1.5, 2, 2.5, 2.25, 3, 10]

#Make Networth
def EarnMoney():
    global score
    score += rate
    showMoney.config(text="You have $" + str(score))
    status.config(text="Status: You earned Money.")
    if score > 10000:
        scam = Button(text="Click Here for more money!", command=lambda: ugotscamed())
        scam.pack(anchor=S)


def BuyStuff(itemName):
    for obj in buy_Obj:
        if obj["name"] == itemName:
            BuyButton.config(text="Buy: $" + str(obj['price']))
        elif itemName == "Pick something to buy":
            BuyButton.config(text="BUY")

def BuyingIt(item):
    global score
    global likenessLevel
    for obj in buy_Obj:
        if obj["name"] == item:
            if score < obj["price"]:
                status.config(text="Status: You Cannot buy this item. You are too poor.")
            else:
                score -= obj["price"]
                showMoney.config(text="You have $" + str(score))
                status.config(text="Status: You Bought an item.")
                boughtItems.append(item)
                showBuy.insert(END, item)
                likenessLevel += obj['like']
                likeness.config(text="People like you at level " + str(likenessLevel))



def HireStuff(itemName):
    for obj in hire_obj:
        if obj["name"] == itemName:
            HireButton.config(text="Hire: $" + str(obj['price']) + " & LL " +str(obj['fame']) + " || + $" +
                                   str(obj['earn']) + " And " + str(obj['sal']) + "x salary.")
        elif itemName == "Pick Something to hire":
            HireButton.config(text="HIRE")

def HiringIt(item):
    global score
    global rate
    global likenessLevel
    for obj in hire_obj:
        if obj["name"] == item:
            if score < obj["price"] or likenessLevel < obj['fame']:
                status.config(text="Status: You Cannot hire this item. You don't have enough money or are not at a high enough Likeness Level.")
            else:
                score -= obj["price"]
                score += obj['earn']
                rate *= obj['sal']
                showMoney.config(text="You have $" + str(score))
                status.config(text="Status: You hired an item.")
                HiredItems.append(item)
                showHire.insert(END, item)
                likenessLevel -= obj['fame']
                likeness.config(text="People like you at level " + str(likenessLevel))
                sala.config(text='Your Salary is $' + str(rate))


def rulez():
    rules.config(text='Back', command=lambda: getridoftext(daRulez))
    daRulez = tk.Label(text='The objective of The Republican Way is to earn all the money you can. \nPressing the \'$\' gets'
                         ' you money by your Salary. \nChoosing an Item and buying it will Level-up your Likeness Level '
                         '(LL). \nChoosing and Hiring an item will either give you money, or raise your salary, but it '
                         'costs likeness Levels.', font=('Times New Roman', 18))
    daRulez.pack(anchor=NW)


def ugotscamed():
    global score
    winningnumber = random.randrange(1,6)
    if winningnumber == 2 or winningnumber == 1:
        score *= random.choice(winmoney)
        showMoney.config(text="You have $" + str(score))
        status.config(text="Status: You got more Money.")
    else:
        score *= random.choice(lossmoney)
        showMoney.config(text="You have $" + str(score))
        status.config(text="Status: You got scammed and lost your Money.")


def getridoftext(daRulez):
    daRulez.config(state=DISABLED)
    daRulez.pack_forget()
    rules.config(text='Rules', command=lambda: rulez())



win = Tk()
win.geometry("1800x1200")
win.title("The Republican Way")
Title = tk.Label(win, text="The Republican Way\n", font=("Times New Roman", 44))
Title.pack()
showMoney = tk.Label(win, text="You have $" + str(score), font=("Times New Roman", 40))
showMoney.pack()
sala = tk.Label(win, text='Your Salary is $' + str(rate), font=('Arial', 32))
sala.pack()
likeness = tk.Label(text="People like you at level " + str(likenessLevel), font=('Arial', 30))
likeness.pack()
status = tk.Label(text="Status: Not Much", font=('Arial', 20))
status.pack()
but = Button(win, text="$",  command=EarnMoney, width=15)
but.pack()

buy_Obj = [{"name": 'Vending Machine Snack', 'price': 2, 'like': 1}, {"name": 'Apple', 'price': 5, 'like': 2},
                    {"name": 'Pack of Pencils', 'price': 10, 'like': 2}, {"name": 'LEGO Set', 'price': 20, 'like': 3},
                    {"name": 'Book', 'price': 25, 'like': 2}, {"name": 'Gift Card', 'price': 50, 'like': 4},
                    {"name": 'Good Shoes', 'price': 100, 'like': 4}, {"name": 'Phone', 'price': 500, 'like': 6},
                    {"name": 'Car', 'price': 50000, 'like': 9}, {"name": 'House', 'price': 500000, 'like': 15},
                    {'name': 'Mansion', 'price': 50000000, 'like': 20}, {'name': 'Island', 'price': 100000000, 'like': 50}]
buyObjNames = ["Pick something to buy"]
for obj in buy_Obj:
    buyObjNames.append(obj["name"])
selectedObj = StringVar(win)
selectedObj.set(buyObjNames[0])
BuyButton = Button(text="BUY", command=lambda: BuyingIt(selectedObj.get()))
BuyButton.pack(side=LEFT)
ObjToBuy = OptionMenu(win, selectedObj, *buyObjNames, command=BuyStuff)
ObjToBuy.pack(side=LEFT)


hire_obj = [{"name": 'Lemonade Stand', 'price': 5, 'sal': 1, 'earn': 10, 'fame': 1},
            {'name': 'Car Wash', 'price': 15, 'sal': 1, 'earn': 30, 'fame': 2},
            {'name': 'Car Wash COMPANY', 'price': 100, 'sal': 2, 'earn': 0, 'fame': 10},
            {'name': 'Company', 'price': 300, 'sal': 4, 'earn': 0, 'fame': 50},
            {'name': 'Butler', 'price': 1000000, 'sal': 10, 'earn': 10, 'fame': 200},
            {'name': 'Construction Workers', 'price': 1000000000, 'sal': 3, 'earn': 100, 'fame': 500},
            {'name': 'Oil Rig', 'price': 5000000000000, 'sal': 20, 'earn': 1000, 'fame': 1000}]
hireObjNames = ["Pick Something to hire"]
for obj in hire_obj:
    hireObjNames.append(obj["name"])
HselectedObj = StringVar(win)
HselectedObj.set(buyObjNames[0])
HireButton = Button(text="HIRE", command=lambda: HiringIt(HselectedObj.get()))
HireButton.pack(side=RIGHT)
ObjToHire = OptionMenu(win, HselectedObj, *hireObjNames, command=HireStuff)
ObjToHire.pack(side=RIGHT)

showBuy = Listbox(win)
showBuy.pack(anchor=S)
showBuy.insert(END, "You have bought ",)
showHire = Listbox(win)
showHire.pack(anchor=S)
showHire.insert(END, "You have hired ",)

rules = Button(text='Rules', command=lambda: rulez())
rules.pack(anchor=NW)








win.mainloop()
