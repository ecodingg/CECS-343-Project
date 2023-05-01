import csv
from csv import *
from tkinter import *
from tkinter import messagebox

def expenseRecord():
    global expenseRow
    global mainExpenseList
    global deleted
    deleted = 0
    expenseRow = 0
    mainExpenseList = []

    def addExpense(pd = None, p = None, a = None, bc = None):
        global expenseRow
        global mainExpenseList

        if pd == None and p == None and a == None and bc == None:
            paymentDate = Text(window, height=1, width=16, font=("Arial", 10))
            payee = Text(window, height=1, width=16, font=("Arial", 10))
            amount = Text(window, height=1, width=16, font=("Arial", 10))
            budgetCategory = Text(window, height=1, width=16, font=("Arial", 10))
        else:
            paymentDate = Text(window, height=1, width=16, font=("Arial", 10))
            paymentDate.insert("1.0", pd)

            payee = Text(window, height=1, width=16, font=("Arial", 10))
            payee.insert("1.0", p)

            amount = Text(window, height=1, width=16, font=("Arial", 10))
            amount.insert("1.0", a)

            budgetCategory = Text(window, height=1, width=16, font=("Arial", 10))
            budgetCategory.insert("1.0", bc)
            

        paymentDate.grid(row=2 + expenseRow, column=1, padx=5, pady=10)
        payee.grid(row=2 + expenseRow, column=2, padx=5, pady=10)
        amount.grid(row=2 + expenseRow, column=3, padx=5, pady=10)
        budgetCategory.grid(row=2 + expenseRow, column=4, padx=5, pady=10)

        #when you click the "X" button, deletes the entire row and moves everything up
        def deleteRow():
            if len(paymentDate.get(1.0, "end-1c")) == 0 and len(paymentDate.get(1.0, "end-1c")) == 0 and len(amount.get(1.0, "end-1c")) == 0 and len(budgetCategory.get(1.0, "end-1c")) == 0:
                paymentDate.destroy()
                payee.destroy()
                amount.destroy()
                budgetCategory.destroy()
                deleteButton.destroy()
                updateButton.destroy()
            else:
                expenseRecord = [paymentDate.get(1.0, "end-1c"), payee.get(1.0, "end-1c"),
                            amount.get(1.0, "end-1c"), budgetCategory.get(1.0, "end-1c")]
                mainExpenseList.remove(expenseRecord)

                paymentDate.destroy()
                payee.destroy()
                amount.destroy()
                budgetCategory.destroy()
                deleteButton.destroy()
                updateButton.destroy()

        deleteButton = Button(window, text="X", command = deleteRow)
        deleteButton.grid(row=2 + expenseRow, column=0, padx=5, pady=10)

        #the user cannot click the checkmark twice, otherwise the earth explodes
        def update():
            expenseList=[paymentDate.get(1.0, "end-1c"), payee.get(1.0, "end-1c"),
                        amount.get(1.0, "end-1c"), budgetCategory.get(1.0, "end-1c")]
            mainExpenseList.append(expenseList)

        updateButton = Button(window, text=u"\u2713", command = update)
        updateButton.grid(row=2 + expenseRow, column=5, padx=5, pady=10)

        expenseRow += 1

    def save():

        duplicateCheck = []
        [duplicateCheck.append(x) for x in mainExpenseList if x not in duplicateCheck]

        with open("expenserecord.csv", "w", encoding="UTF8", newline="") as file:
            Writer = writer(file)
            Writer.writerow(["Payment Date", "Payee", "Amount", "Budget Category"])
            for x in duplicateCheck:
                Writer.writerow(x)
            messagebox.showinfo("System", "Saved successfully")

    #PLEASE load first if there is data in the csv file!
    def load():
        with open("expenserecord.csv", 'r') as f:
            csv_reader = csv.reader(f)
            for line_no, line in enumerate(csv_reader, 1):
                if line_no == 1:
                    pass
                else:
                    addExpense(line[0], line[1], line[2], line[3])
                    expenseRecord = [line[0], line[1], line[2], line[3]]
                    mainExpenseList.append(expenseRecord)
        loadButton.destroy()

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

    addButton = Button(window, text="Add Expense", command=addExpense)
    addButton.grid(row=100, column=2)

    saveButton = Button(window, text="Save", command=save)
    saveButton.grid(row=100, column=3)

    loadButton = Button(window, text="Load Saved File", command=load)
    loadButton.grid(row=100, column=4)

    window.mainloop()

def sumExpense():
    sum = 0
    with open("expenserecord.csv", 'r') as f:
        csv_reader = csv.reader(f)
        for line_no, line in enumerate(csv_reader, 1):
            if line_no == 1:
                pass
            else:
                sum += float(line[2])
    return sum
    
def sumBudget():
    list = dict()
    with open("expenserecord.csv", 'r') as f:
        csv_reader = csv.reader(f)
        for line_no, line in enumerate(csv_reader, 1):
            if line_no == 1:
                pass
            else:
                if (line[3] in list):
                    num = float(list[line[3]])
                    num += float(line[2])
                    list[line[3]] = str(num)
                else:
                    list.update({line[3]: line[2]})
    return list




    #FOR ANNUAL SUMMARY
    #test = sumBudget()
    #for i in test:
    #    print(i + ": $" + str(format(float(test[i]), '.2f')))

#expenseRecord()


