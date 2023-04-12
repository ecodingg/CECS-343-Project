
from tkinter import *

def editExpense():
    print("WORK")
def submitChange():
    print("WORK")
window = Tk()
titleLabel = Label(window, text="Expense Record", font=("Arial", 16), padx=10, pady=10)
titleLabel.grid(row=0, column=0, columnspan=6, sticky="N")
paymentDateLabel = Label(window, text="Payment Date", font=("Arial", 14), padx=10, pady=10)
payeeLabel = Label(window, text="Payee", font=("Arial", 14), padx=10, pady=10)
amountLabel = Label(window, text="Amount", font=("Arial", 14), padx=10, pady=10)
categoryLabel = Label(window, text="Budget Category", font=("Arial", 14), padx=10, pady=10)
paymentDateLabel.grid(row = 1, column=0)
payeeLabel.grid(row = 1, column=1)
amountLabel.grid(row = 1, column=2)
categoryLabel.grid(row = 1, column=3)
editButton = Button(window, text="Edit", command=editExpense)
editButton.grid(row=100, column=0, columnspan=2, sticky="n")
submitButton = Button(window, text="Submit Changes", command= submitChange)
submitButton.grid(row=100, column=3, columnspan=2, sticky="n")
window.mainloop()