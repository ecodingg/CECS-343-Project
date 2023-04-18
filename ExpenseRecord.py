from csv import *
from tkinter import *
from tkinter import messagebox

global expenseRow
global mainExpenseList
global deleted
deleted = 0
expenseRow = 0
mainExpenseList = []

def addExpense():
    global expenseRow
    global mainExpenseList

    paymentDate = Text(window, height=1, width=16, font=("Arial", 10))
    payee = Text(window, height=1, width=16, font=("Arial", 10))
    amount = Text(window, height=1, width=16, font=("Arial", 10))
    budgetCategory = Text(window, height=1, width=16, font=("Arial", 10))

    paymentDate.grid(row=2 + expenseRow, column=1, padx=5, pady=10)
    payee.grid(row=2 + expenseRow, column=2, padx=5, pady=10)
    amount.grid(row=2 + expenseRow, column=3, padx=5, pady=10)
    budgetCategory.grid(row=2 + expenseRow, column=4, padx=5, pady=10)

    #when you click the "X" button, deletes the entire row and moves everything up
    #figure out why indexes are wrong
    def deleteRow():
        global deleted
        index = paymentDate.grid_info()["row"] - 2 - deleted
        print(index)
        if len(mainExpenseList) == 1:
            mainExpenseList.pop(0)
        else:
            mainExpenseList.pop(index)

        paymentDate.destroy()
        payee.destroy()
        amount.destroy()
        budgetCategory.destroy()
        deleteButton.destroy()
        updateButton.destroy()

        deleted += 1

    deleteButton = Button(window, text="X", command = deleteRow)
    deleteButton.grid(row=2 + expenseRow, column=0, padx=5, pady=10)

    def update():
        expenseList=[paymentDate.get(1.0, "end-1c"), payee.get(1.0, "end-1c"), 
                    amount.get(1.0, "end-1c"), budgetCategory.get(1.0, "end-1c")]
        mainExpenseList.append(expenseList)

    updateButton = Button(window, text=u"\u2713", command = update)
    updateButton.grid(row=2 + expenseRow, column=5, padx=5, pady=10)

    expenseRow += 1

def save():
    with open("expenserecord.csv", "w") as file:
        Writer = writer(file)
        Writer.writerow(["Payment Date", "Payee", "Amount", "Budget Category"])
        Writer.writerow(mainExpenseList)
        messagebox.showinfo("System", "Saved successfully")

window = Tk()
titleLabel = Label(window, text="Expense Record", font=("Arial", 16), padx=10, pady=10)
titleLabel.grid(row=0, column=0, columnspan=6, sticky="N")

paymentDateLabel = Label(window, text="Payment Date", font=("Arial", 14), padx=10, pady=10)
payeeLabel = Label(window, text="Payee", font=("Arial", 14), padx=10, pady=10)
amountLabel = Label(window, text="Amount", font=("Arial", 14), padx=10, pady=10)
categoryLabel = Label(window, text="Budget Category", font=("Arial", 14), padx=10, pady=10)

paymentDateLabel.grid(row = 1, column=1)
payeeLabel.grid(row = 1, column=2)
amountLabel.grid(row = 1, column=3)
categoryLabel.grid(row = 1, column=4)

saveButton = Button(window, text="Save", command=save)
saveButton.grid(row=100, column=3)

addButton = Button(window, text="Add Expense", command=addExpense)
addButton.grid(row=100, column=2)

window.mainloop()
