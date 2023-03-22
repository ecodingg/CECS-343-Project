from tkinter import *
from menu import menu


def login():
   loginInput()
   #Check that Login is accurate
   if (loginValidation):
      menu()
   else:
      print("Sorry that is the wrong Username and Password")

   
    


def loginInput():
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
   return loginText, passwordText
   top.mainloop()

def loginValidation():
   #Checks that the input for Login is Valid
   print("This is not done yet")
   
