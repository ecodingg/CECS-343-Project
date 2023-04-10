from tkinter import *
#import XML
#import beautifulsoup
from menu import menu


def login():
   loginInfo = loginInput()
   #Check that Login is accurate
   if (loginValidation(loginInfo)):
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
   username = loginButton
   password = passwordButton
   top.mainloop()
   return username, password
   

def loginValidation():
   #Checks that the input for Login is Valid
   print("This is not done yet")
   
