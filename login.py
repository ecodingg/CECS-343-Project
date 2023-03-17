from tkinter import *
from menu import menu


def login():
   #Need to Check if 
   top = Tk()
   loginText = Label(top, text="User Name")
   loginText.pack( side = LEFT)
   loginButton = Entry(top, bd =5)
   loginButton.pack(side = LEFT)
   passwordText = Label(top, text="Password")
   passwordText.pack( side = LEFT)
   passwordButton = Entry(top, bd =5)
   passwordButton.pack(side = LEFT)

   #Check that Login is accurate

   menu()
   top.mainloop() 


