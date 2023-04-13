from tkinter import *
  
  
def menu():
    root = Tk()

    B1 = root.Button(top, text="Expense Record", command=expenseButton())
    B1.pack()

    B2 = root.Button(top, text="Tenant List", command=tenantButton())
    B2.pack()

    B3 = root.Button(top, text="Rental Record", command=rentalButton())
    B3.pack()

    B4 = root.Button(top, text="Expense Record", command=annualButton())
    B4.pack()


    root.mainloop()

def expenseButton():
    print("Not done")


def annualButton():
    print("Not done")

def tenantButton():
    print("Not done")

def rentalButton():
    print("Not done")