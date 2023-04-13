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

<<<<<<< Updated upstream
def loginValidation():
   #Checks that the input for Login is Valid
   print("This is not done yet")
=======
   username = loginButton
   password = passwordButton

   test = loginCredentials()

   if (test):
      # credentials = LoginInfo()
      # credentials.username = username
      # credentials.password = password
   
      f = open("loginInfo.txt", "w")
      f.write(username)
      f.write("\n")
      f.write(password)
      f.close()
   
   else:
      testTwo = loginValidation(username, password)
      if (testTwo):
         menu()
      else:
         print("Try to login again")

   top.mainloop()
   

   
   
#Checks to see that Login works
def loginValidation(user, passW):
   f = open("loginInfo.txt", "w")
   loginArray = []
   
   for i in range(1,3):
      loginArray.append(f.readline())

   if (user == loginArray[1]):
      if(passW == loginArray[2]):
         return True
   else:
      print("Incorrect Login Credentials")
      return False


def loginCredentials():
   f = open("loginInfo.txt", "w")
   if (len(f.read()) == 0):
      return True
   else:
      return False
   
>>>>>>> Stashed changes
   
