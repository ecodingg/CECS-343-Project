import tkinter as tk
from tkinter import ttk
from tenant import *
  
  
def menu():
    root = tk.Tk()
    root.title("Tab Widget")
    tabControl = ttk.Notebook(root)
    
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    
    tabControl.add(tab1, text ='Tenant List')
    tabControl.add(tab2, text ='Rental Income Record')
    tabControl.add(tab3, text='Expense Record')
    tabControl.add(tab4, text='Annual Summary')
    tabControl.pack(expand = 1, fill ="both")
    addTenantButton = Button(root, text="Add Tenant", command=startTenantList)
    addTenantButton.pack()


    root.mainloop()
    