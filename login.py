from tkinter import *
from menu import menu


class LoginInfo:
   username: str
   password: str



def login():
   LoginInput()

   

def LoginInput():
   #Inputting Login Credentials 
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

   username = loginButton
   password = passwordButton

   test = loginCredentials()

   if (test):
      loginCredentials = LoginInfo()
      loginCredentials.username = username
      loginCredentials.password = password
   
      f = open("loginInfo.txt", "w")
      f.write(username)
      f.write("\n")
      f.write(password)
      f.close()
   
      top.mainloop()
      return loginCredentials
   else:
      testTwo = loginValidation(username, password)
      if (testTwo):
         menu()
      else:
         print("Try to login again")


   
   
#Checks to see that Login works
def loginValidation(user, passW):
   f = open("loginInfo.txt", "r")
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
   f = open("loginInfo.txt", "r")
   if (len(f.read()) == 0):
      return True
   else:
      return False
   
   
