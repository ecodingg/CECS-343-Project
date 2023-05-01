import csv
from csv import *
from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
from menu import menu

def login():
   root = tk.Tk()

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

   def verify():
      user = loginButton.get(1.0, "end-1c")
      password = passwordButton.get(1.0, "end-1c")
      userCheck = False
      passwordCheck = False
      with open("loginInfo.csv", 'r', encoding="UTF-8", newline="") as f:
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
            f.close()
            with open("loginInfo.csv", 'a', encoding="UTF-8", newline="") as d:
               if (os.stat("loginInfo.csv").st_size == 0):
                  Writer = writer(d)
                  Writer.writerow([user])
                  Writer.writerow([password])
                  root.destroy()
                  menu()
               else:
                  messagebox.showinfo("System", "Incorrect username or password.")

   submitButton = Button(root, bd =5, text="Login", command=verify)
   submitButton.pack(side = BOTTOM)

   root.mainloop()

