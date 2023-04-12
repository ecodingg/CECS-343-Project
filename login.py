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
   frame = Frame(top)
   frame.pack()
   bottomframe = Frame(top)
   bottomframe.pack(side = BOTTOM)
   loginText = Label(top, text="User Name")
   loginText.pack( side = LEFT)
   loginButton = Entry(top, bd =4)
   loginButton.pack(side = LEFT)
   passwordText = Label(top, text="Password")
   passwordText.pack( side = LEFT)
   passwordButton = Entry(top, bd =4)
   passwordButton.pack(side = LEFT)
   submitButton = Button(bottomframe, text="Submit")
   submitButton.pack( side = BOTTOM)
   return loginText, passwordText, submitButton
   top.mainloop()

def loginValidation():
   #Checks that the input for Login is Valid
   print("This is not done yet")
   
