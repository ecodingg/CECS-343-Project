from ExpenseRecord import *
from tenant import *

def annualSummary():
    window = Tk()

    titleLabel = Label(window, text="Annual Summary", font=("Arial bold", 16), padx=10, pady=10)
    titleLabel.grid(row=0, column=0, columnspan=6, sticky="N")

    budgetCategories = sumBudget()
    budgetDetails = ""
    for i in budgetCategories:
        budgetDetails += (i + ": $" + str(format(float(budgetCategories[i]), '.2f')) + "\n")

    netTotal = returnRentalIncome() - sumExpense()
    totalIncome = Label(window, text="Total income: $" + str(returnRentalIncome()), font=("Arial", 14), padx=10, pady=10)
    totalExpenses = Label(window, text="Total expenses: $" + str(sumExpense()), font=("Arial", 14), padx=10, pady=10)
    expenseDetails = Label(window, text="Expense details: \n" + budgetDetails, font=("Arial", 14), padx=10, pady=10)
    net = Label(window, text="Profit/Loss: $" + str(netTotal), font=("Arial", 14), padx=10, pady=10)

    totalIncome.grid(row = 1, column=1)
    totalExpenses.grid(row = 2, column=1)
    expenseDetails.grid(row = 3, column=1)
    net.grid(row = 4, column=1)

    window.mainloop()
