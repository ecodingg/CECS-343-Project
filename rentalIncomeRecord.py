from tkinter import *
from tenant import Tenant
import csv
tenants = []

def removeTenant(email):
    for ten in tenants:
        if(ten.email == email):
            tenants.remove(ten)
def removeRow(email):
    removeTenant(email)
    for label in window.winfo_children():
        label.destroy()
    startWindow()

def readData():
    f = open("tenantTest.txt","r")
    for x in f:
        split = x.split(",")
        resident = Tenant(split[0],split[1],split[2],split[3],split[4],split[5],split[6],split[7],split[8])
        tenants.append(resident)
    f.close()
def saveData():
    f = open("tenantTest.txt","w")
    for tenant in tenants:
        f.write(tenant.firstName + "," + tenant.lastName + "," + tenant.email + "," + tenant.age + ",")
        f.write(tenant.rent + "," + tenant.apt + "," + tenant.payDue + "," + tenant.paidDate + "," + tenant.onTime )
    f.close()

def writeTenants(): #reads TenantLists and make chart in window
    # print("READ FROM THE LIST AND ADD THEM")
    tRow = 2
    for ten in range(len(tenants)):
        tenant = tenants[ten]
        tName = Label(window, text=tenant.firstName + " " + tenant.lastName, font=("Arial", 14), padx=10, pady=10)
        tName.grid(row = tRow, column = 0)
        tRent = Label(window, text=tenant.rent, font=("Arial", 14), padx=10, pady=10)
        tRent.grid(row = tRow, column=1)
        tPDD = Label(window, text = tenant.paymentDueDate, font=("Arial", 14), padx=10, pady=10)
        tPDD.grid(row=tRow, column=2)
        tPD = Label(window, text = tenant.paymentDate , font=("Arial", 14), padx=10, pady=10)
        tPD.grid(row = tRow, column=3)
        tOnTime = Label(window, text = tenant.isPaid, font=("Arial", 14), padx=10, pady=10)
        tOnTime.grid(row=tRow, column=4)
        delete = Button(window, text = 'X', command=lambda email = tenant.email: removeRow(email))
        delete.grid(row = tRow, column = 5)
        tRow = tRow +1

def editRecord():
    tRow = 2
    for ten in range(len(tenants)):
        tenant = tenants[ten]
        tName = Entry(window)
        tName.insert(0, tenant.firstName + " " + tenant.lastName)
        tName.grid(row = tRow, column = 0)
        tRent = Entry(window)
        tRent.insert(0, tenant.rent)
        tRent.grid(row = tRow, column=1)
        tPDD = Entry(window)
        tPDD.insert(0, tenant.paymentDueDate)
        tPDD.grid(row=tRow, column=2)
        tPD = Entry(window)
        tPD.insert(0,tenant.paymentDate)
        tPD.grid(row = tRow, column=3)
        tOnTime = Entry(window)
        tOnTime.insert(0,tenant.isPaid)
        tOnTime.grid(row=tRow, column=4)

        tRow = tRow +1

def save():
    counter = 0
    for label in window.winfo_children():
        if(type(label) == Entry):

            person = counter//5
            section = counter%5
            if (section ==0 ):
                firstName = label.get().split()[0]
                lastName = label.get().split()[1]
                # print("First: "+ firstName)
                # print( label.get().split())
                # print("LAst: " + lastName)
                tenants[person].firstName = firstName
                tenants[person].lastName = lastName
            elif (section ==1):
                tenants[person].rent = label.get()
            elif (section ==2):
                tenants[person].payDue = label.get()
            elif (section ==3):
                tenants[person].paidDate = label.get()
            elif (section ==4):
                tenants[person].onTime = label.get()

            counter = counter +1
    for label in window.winfo_children():
        label.destroy()
    startWindow()
def addTenantRow():
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


window = Tk()
def startWindow():
    titleLabel = Label(window, text="Rental Income Record", font=("Arial", 16), padx=10, pady=10)
    titleLabel.grid(row=0, column=0, columnspan=6, sticky="N")

    nameLabel = Label(window, text="Name", font=("Arial", 14), padx=10, pady=10)
    rentLabel = Label(window, text="Rent", font=("Arial", 14), padx=10, pady=10)
    dueDatelLabel = Label(window, text="Payment Due Date", font=("Arial", 14), padx=10, pady=10)
    payDateLabel = Label(window, text="Payment Date", font=("Arial", 14), padx=10, pady=10)
    timeLabel = Label(window, text="On Time? (Y/N)", font=("Arial", 14), padx=10, pady=10)

    nameLabel.grid(row = 1, column=0)
    rentLabel.grid(row = 1, column=1)
    dueDatelLabel.grid(row = 1, column=2)
    payDateLabel.grid(row = 1, column=3)
    timeLabel.grid(row = 1, column=4)

    editButton = Button(window, text="Edit", command=editRecord)
    editButton.grid(row=100, column=0, columnspan=2, sticky="n")
    saveButton = Button(window, text="Save", command=save)
    saveButton.grid(row=100, column=4, columnspan=2, sticky="n")
    saveFile = Button(window, text="Save To File", command = saveData)
    saveFile.grid(row=100, column =2, columnspan =2,  sticky = "n")

    writeTenants()
    window.mainloop()

def main():
    readData()
    startWindow()

if __name__ == "__main__":
    main()