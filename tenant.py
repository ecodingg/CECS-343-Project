from tkinter import * 
from tkinter import simpledialog
import csv

global tenantRow
tenantRow = 0

class Tenant:
    def __init__(self, firstName, lastName, email, age, rent, apt):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.age = age
        self.rent = rent
        self.apt = apt

    def __iter__(self):
        return iter([self.firstName, self.lastName, self.email, self.age, self.rent, self.apt])
    
    def __str__(self):
        return f"{self.firstName}, {self.lastName}, {self.email}, {self.age}, {self.rent}, {self.apt}"

def removeTenantRow(window):
    name = simpledialog.askstring("User Input", "Please enter the First Name: ")
    if name is None:
        return
        
    # get integer input
    aptNumber = simpledialog.askinteger("User Input", "Enter the Apartment #: ")
    if aptNumber is None:
        return
    #remove row with firstname & apt#
    
        

def addTenantRow(window):
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
    # newFirstName = simpledialog.askstring("User Input", "Please enter the First Name: ")
    # newLastName = simpledialog.askstring("User Input", "Please enter the Last Name: ")
    # newEmail = simpledialog.askstring("User Input", "Please enter the email: ")
    # newAge = simpledialog.askstring("User Input", f"Please enter {newFirstName}'s age: ")
    # newRent = simpledialog.askstring("User Input", "Please enter the Rent amount: ")
    # newApt = simpledialog.askstring("User Input", "Please enter the apt#: ")


    tenantRow += 1


def saveTenants(window):
    tenantEntries = []
    tenantList = []
    for r in range(2, tenantRow):
        for c in range(0, 6):
            cell = Entry(window)
            cell.grid(row=r, column=c)
            print(cell.get())
            tenantEntries.append(cell.get())
        tenant = Tenant(tenantEntries[0], tenantEntries[1], tenantEntries[2], tenantEntries[3], tenantEntries[4], tenantEntries[5])
        tenantEntries.clear()
        tenantList.append(tenant)

    print(tenantList)
    with open("tenantTest.txt", "w", newline="") as stream:
        writer = csv.writer(stream)
        for entry in tenantList:
            writer.writerow(entry)


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
    addTenantButton = Button(window, text="Add Tenant", command=lambda: addTenantRow(window))
    addTenantButton.grid(row=100, column=0, columnspan=2, sticky="n")
    # create save button
    addTenantButton = Button(window, text="Save", command=lambda: saveTenants(window))
    addTenantButton.grid(row=100, column=2, columnspan=3, sticky="n")
    removeTenantButton = Button(window, text="Remove Tenant", command=lambda: removeTenantRow(window))
    removeTenantButton.grid(row=100, column=4, columnspan=2, sticky="n")

    window.mainloop()
