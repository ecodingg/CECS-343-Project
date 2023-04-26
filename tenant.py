from tkinter import * 
from tkinter import simpledialog
import csv

global tenantRow
tenantRow = 0


class Tenant:
    def __init__(self, firstName, lastName, email, age, rent, apt, paymentDueDate, paymentDate, isPaid):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.age = age
        self.rent = rent
        self.apt = apt
        self.paymentDueDate = paymentDueDate
        self.paymentDate = paymentDate
        self.isPaid = isPaid

    def __iter__(self):
        return iter([self.firstName, self.lastName, self.email, self.age, self.rent, self.apt, self.paymentDueDate, self.paymentDate, self.isPaid])
    
    def __str__(self):
        return f"{self.firstName}, {self.lastName}, {self.email}, {self.age}, {self.rent}, {self.apt}, {self.paymentDueDate}, {self.paymentDate}, {self.isPaid}"
    


#keep working to get rid of bug
def removeTenantRow(window):
    global tenantRow
    name = simpledialog.askstring("User Input", "Please enter the First Name: ")
    if name is None:
        return
        
    # get integer input
    aptNumber = simpledialog.askinteger("User Input", "Enter the Apartment #: ")
    if aptNumber is None:
        return
    # remove row with firstname & apt#
    # works similar to the add tenant row but will delete row if 
    # both firstname and aptnumber are in that specific row
    for r in range(2,2 + tenantRow):
        rowEntries = []
        for c in range(0, 6):
            entry = window.grid_slaves(row=r, column=c)[0]
            rowEntries.append(entry)

        if rowEntries[0].get() == name and int(rowEntries[5].get()) == aptNumber:
            #delete the entire row
            for value in window.grid_slaves(row=r):
                value.destroy()
            # update row numbers
            for k in range(r+1, 2 + tenantRow):
                for l in range(6):
                    widget = window.grid_slaves(row=k, column=l)[0]
                    widget.grid(row=k-1, column=l,padx=5, pady=10)
            tenantRow -= 1
            break
            

def addTenantRow(window,saveTenantButton, addTenantButton, removeTenantButton):
    global tenantRow
    newFirstName = Entry(window)
    newLastName = Entry(window)
    newEmail = Entry(window)
    newAge = Entry(window)
    newRent = Entry(window)
    newApt = Entry(window)

    newFirstName.grid(row=2 + tenantRow, column=0, padx=5, pady=10)
    newLastName.grid(row=2 + tenantRow, column=1, padx=5, pady=10)
    newEmail.grid(row=2 + tenantRow, column=2, padx=5, pady=10)
    newAge.grid(row=2 + tenantRow, column=3, padx=5, pady=10)
    newRent.grid(row=2 + tenantRow, column=4, padx=5, pady=10)
    newApt.grid(row=2 + tenantRow, column=5, padx=5, pady=10)

    tenantRow += 1
    addTenantButton.grid(row=2 + tenantRow, column=0, columnspan=2, sticky="n")
    saveTenantButton.grid(row=2 + tenantRow, column=2, columnspan=2, sticky="n")
    removeTenantButton.grid(row=2 + tenantRow, column=4, columnspan=2, sticky="n")

def saveTenants(window):
    #create an empty list to save all tenants
    tenantList = []
    for r in range(2, 2 + tenantRow):
        #this list will save the entries of each row
        tenantEntries = []
        for c in range(0, 6):
            entry = window.grid_slaves(row=r, column=c)[0]
            tenantEntries.append(entry.get())
        tenant = Tenant(tenantEntries[0], tenantEntries[1], tenantEntries[2], tenantEntries[3], tenantEntries[4], tenantEntries[5], "None", "None", "None")
        tenantEntries.clear()
        tenantList.append(tenant)

    # add last 3 entries from csv to prevent them from being overwritten
    with open('tenantTest.txt', 'r') as input:
        reader = csv.reader(input)
        rows = list(reader)
    # go through all current rows on screen
    for i in range(len(tenantList)):
        # will loop through all loops to find the correct one and add last three entries
        for j in range(len(rows)):
            row = rows[j]
            if (tenantList[i].firstName == row[0] and tenantList[i].apt == row[5]):
                tenantList[i].paymentDueDate = row[6]
                tenantList[i].paymentDate = row[7]
                tenantList[i].isPaid = row[8]
            

    # save list to a csv
    with open('tenantTest.txt', 'w', newline='') as output:
        writer = csv.writer(output)
        for entry in tenantList:
            writer.writerow(entry)


def populateList(window, saveTenantButton, addTenantButton, removeTenantButton):
    global tenantRow
    with open('tenantTest.txt', newline='') as input:
        reader = csv.reader(input)

        # iterate over each row in the CSV file
        for i, row in enumerate(reader):
            # create a new row in the grid
            for j, value in enumerate(row):
                # create an Entry widget with the value from the CSV file
                entry = Entry(window)
                entry.grid(row=i+2, column=j, padx=5, pady=10)
                # set the value of the Entry widget to the value from the CSV file
                entry.insert(0, value)
                if j == 5: break
                
            tenantRow += 1

    addTenantButton.grid(row=2 + tenantRow, column=0, columnspan=2, sticky="n")
    saveTenantButton.grid(row=2 + tenantRow, column=2, columnspan=2, sticky="n")
    removeTenantButton.grid(row=2 + tenantRow, column=4, columnspan=2, sticky="n")



def startTenantList():
    
    window = Tk()

    # The Tenant List title displayed front and Center
    titleLabel = Label(window, text="Tenant List", font=("Arial", 16), padx=10, pady=10)
    titleLabel.grid(row=0, column=0, columnspan=6, sticky="N")

    # create 6 columns for the tenant list
    firstNameLabel = Label(window, text="First Name", font=("Arial", 14), padx=10, pady=10)
    lastNameLabel = Label(window, text="Last Name", font=("Arial", 14), padx=10, pady=10)
    emailLabel = Label(window, text="Email", font=("Arial", 14), padx=10, pady=10)
    ageLabel = Label(window, text="Age", font=("Arial", 14), padx=10, pady=10)
    rentLabel = Label(window, text="Rent", font=("Arial", 14), padx=10, pady=10)
    aptLabel = Label(window, text="Apt #", font=("Arial", 14), padx=10, pady=10)

    # lay them out side by side
    row1 = 1
    firstNameLabel.grid(row=row1, column=0)
    lastNameLabel.grid(row=row1, column=1)
    emailLabel.grid(row=row1, column=2)
    ageLabel.grid(row=row1, column=3)
    rentLabel.grid(row=row1, column=4)
    aptLabel.grid(row=row1, column=5)

    # create add button
    addTenantButton = Button(window, text="Add Tenant", command=lambda: addTenantRow(window, saveTenantButton, addTenantButton, removeTenantButton))
    addTenantButton.grid(row=2 + tenantRow, column=0, columnspan=2, sticky="n")
    # create save button
    saveTenantButton = Button(window, text="Save", width=30, command=lambda: saveTenants(window))
    saveTenantButton.grid(row=2 + tenantRow, column=2, columnspan=2, sticky="n")
    removeTenantButton = Button(window, text="Remove Tenant", command=lambda: removeTenantRow(window))
    removeTenantButton.grid(row=2 + tenantRow, column=4, columnspan=2, sticky="n")
    # populate list from a csv
    populateList(window, saveTenantButton, addTenantButton, removeTenantButton)
    window.mainloop()

startTenantList()
