import csv
from csv import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from menu import menu

def login():
   root = tk.Tk()
   #These are string inputs for buttons
   username = tk.StringVar()
   password = tk.StringVar()

   introText = Label(root, text="Welcome!")
   loginText = Label(root, text="User Name")
   introText.pack(side = TOP)
   loginText.pack( side = LEFT)
   loginButton = Text(root, height=1, width=16, font=("Arial", 10))
   loginButton.pack(side = LEFT)
   passwordText = Label(root, text="Password")
   passwordText.pack(side = LEFT)
   passwordButton = Text(root, height=1, width=16, font=("Arial", 10))
   passwordButton.pack(side = LEFT)
   return loginText, passwordText
   top.mainloop()

   def verify():
      user = loginButton.get(1.0, "end-1c")
      password = passwordButton.get(1.0, "end-1c")
      userCheck = False
      passwordCheck = False
      with open("loginInfo.csv", 'r') as f:
         csv_reader = csv.reader(f)
         for line_no, line in enumerate(csv_reader, 1):
            if line_no == 1:
               if user == line[0]:
                  userCheck = True
            if line_no == 2:
               if password == line[0]:
                  passwordCheck = True
         if (userCheck) and (passwordCheck):
               root.destroy()
               menu()
         else:
            #If nothing in loginINfo.csv
            messagebox.showinfo("System", "Incorrect username or password.")
   
   submitButton = Button(root, bd =5, text="Login", command=verify)
   submitButton.pack(side = BOTTOM)

   root.mainloop()

