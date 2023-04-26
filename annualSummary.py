
from tkinter import *
#from tenant import Tenant

def startWindow():
    window = Tk()
    window.title("Annual Sumamry")
    titleLabel = Label(window, text="Annual Summary Report", font=("Arial", 16), padx=10, pady=10)
    titleLabel.grid(row=0, column=0, columnspan=6, sticky="N")
    addMoney = 10.00
    lessMoney = 10.00
    mortgage = 30.00
    utility = 40.00
    inMoney = Label(window, text="Incoming Money: $" + str(addMoney), font=("Arial", 14), padx=10, pady=10)
    outMoney = Label(window, text="Outgoing Costs: $" + str(lessMoney) , font=("Arial", 14), padx=10, pady=10)
    mort = Label(window, text="    -Mortgage: $"+ str(mortgage), font=("Arial", 14), padx=10, pady=10)
    util = Label(window, text="    -Utility : $" + str(utility), font=("Arial", 14), padx=10, pady=10)
    total = Label(window, text="Total Revenue: $"+ str(addMoney - lessMoney),font=("Arial", 14), padx=10, pady=10)
    #time = Label(window, text="On Time? (Y/N)", font=("Arial", 14), padx=10, pady=10)

    titleLabel.grid(row = 0, column=0)
    inMoney.grid(row = 3, column=0)
    outMoney.grid(row = 5, column=0)
    mort.grid(row = 7, column =0)
    util.grid(row = 8, column = 0)
    total.grid(row = 13, column = 0)
    window.mainloop()
startWindow()