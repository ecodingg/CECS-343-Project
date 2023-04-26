from tkinter import *
import tkinter as tk
import os
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
   loginButton = Entry(root, bd =5, textvariable=username)
   loginButton.pack(side = LEFT)
   passwordText = Label(root, text="Password")
   passwordText.pack(side = LEFT)
   passwordButton = Entry(root, bd =5, textvariable=password)
   passwordButton.pack(side = LEFT)

   root.mainloop()
   if (loginCredentials() == True):
      f = open("loginInfo.txt", "w", encoding="UTF8", newline="")
      #This is how you write it to file
      f.write(username.get())
      f.write("\n")
      f.write(password.get())
      f.close()

      root.destroy()
      menu()
   else:
      if (loginValidation(username.get(), password.get())):
         root.destroy()
         menu()
      else:
         print("Try to login again")

   
#Checks to see that Login works
def loginValidation(user, passW):
   f = open("loginInfo.txt", "r", encoding="UTF8", newline="")
   loginArray = []
   content = f.readlines()
   
   loginArray.append(content[0])
   loginArray.append(content[1])
   
   print(user)

   if (user == loginArray[0]):
      if(passW == loginArray[1]):
         return True
   else:
      return False


def loginCredentials():
   loginSize = os.stat("loginInfo.txt").st_size
   if (loginSize == 0):
      return True
   else:
      print("Incorrect Password")
      return False
   
   
