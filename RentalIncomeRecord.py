
from tkinter import *
from tenant import Tenant

"""INITIALIZED SOME OF TENANTS TO PRACTICE MAKING CHART. FOR THIS TO WORK, 
        def __init__(self,first,last,email,age,rent,apt):
        self.firstName = first
        self.lastName = last
        self.email = email
        self.age = age
        self.rent = rent
        self.apt = apt
    must be added to tenant class
"""
kevin = Tenant("kevin","lee","Example@gmail.com",24,1400,1)
sarah = Tenant("sarah","chang","sc@gmail.com",22,1200,2)
shaco = Tenant("shaco","bao","clown@gmail.com",24,1600,3)
garen = Tenant("garen","demacia","gdemacia@gmail.com",25,1400,4)
lux = Tenant("lux","light","lightwillguide@gmail.com",28,1200,5)
practice = [kevin,sarah,shaco,garen,lux]

def removeTenant(email):
    for ten in practice:
        if(ten.email == email):
            practice.remove(ten)
def removeRow(email):
    removeTenant(email)
    for label in window.winfo_children():
        label.destroy()
    startWindow()

def writeTenants(): #reads TenantLists and make chart in window
    # print("READ FROM THE LIST AND ADD THEM")
    tenants = practice #IN THE FUTURE NEED FUNCTION TO BRING LIST OF TENANTS FROM STORED DATA
    tRow = 2
    for ten in range(len(tenants)):
        tenant = tenants[ten]
        tName = Label(window, text=tenant.firstName + " " + tenant.lastName, font=("Arial", 14), padx=10, pady=10)
        tName.grid(row = tRow, column = 0)
        tRent = Label(window, text=tenant.rent, font=("Arial", 14), padx=10, pady=10)
        tRent.grid(row = tRow, column=1)
        tPDD = Label(window, text = "WORKLATER", font=("Arial", 14), padx=10, pady=10)
        tPDD.grid(row=tRow, column=2)
        tPD = Label(window, text = "PAYY DATE" , font=("Arial", 14), padx=10, pady=10)
        tPD.grid(row = tRow, column=3)
        tOnTime = Label(window, text = "ONTIME?", font=("Arial", 14), padx=10, pady=10)
        tOnTime.grid(row=tRow, column=4)
        delete = Button(window, text = 'X', command=lambda email = tenant.email: removeRow(email))
        delete.grid(row = tRow, column = 5)
        tRow = tRow +1

def editRecord():
    tenants = practice #IN THE FUTURE NEED FUNCTION TO BRING LIST OF TENANTS FROM STORED DATA
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
        tPDD.insert(0, "DUEDATE")
        tPDD.grid(row=tRow, column=2)
        tPD = Entry(window)
        tPD.insert(0,"PAID DATE")
        tPD.grid(row = tRow, column=3)
        tOnTime = Entry(window)
        tOnTime.insert(0,"LATER WORK")
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
                practice[person].firstName = firstName
                practice[person].lastName = lastName
            elif (section ==1):
                practice[person].rent = label.get()
            # elif (section ==2):
            #
            # elif (section ==3):
            #
            # elif (section ==4):

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
    editButton = Button(window, text="Save", command=save)
    editButton.grid(row=100, column=3, columnspan=2, sticky="n")
    writeTenants()
    window.mainloop()
startWindow()