from tkinter import *
from ExpenseRecord import *
from tenant import *
from rentalIncomeRecord import *
  

def menu():
    window = Tk()
    titleLabel = Label(window, text="Menu", font=("Arial", 14), padx=10, pady=10)
    titleLabel.grid(row=0, column=0, columnspan=6, sticky="N")

    tenantButton = Button(window, text="View Tenant List", command=lambda: [startTenantList()])
    tenantButton.grid(row=1, column=2)
    
    rentalButton = Button(window, text="View Rental Income Record", command=lambda: [rentalIncome()])
    rentalButton.grid(row=2, column=2)
    
    expenseButton = Button(window, text="View Expense Record", command=lambda: [expenseRecord()])
    expenseButton.grid(row=3, column=2)

    annualButton = Button(window, text="View Annual Summary")
    annualButton.grid(row=4, column=2)

    window.mainloop()
