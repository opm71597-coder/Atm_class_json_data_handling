import json
from random import randint
import os

class ATM:
    id_r=str(randint(11111,99999))
    def create(self):
     print("====wellcome to omni bank=======")
     while True:
      name_=input("enter your username :").strip()
      if(name_==""):
       print("set a user first")
      elif(len(name_) +1 < 4):
       print("make at last 4 calrcter username")
      elif(name_.isdigit()):
       print("you can't use only numbers in user name ")
      elif(name_=="exit"):
       return
      else:
       break
     while True:
      try:
       age_=int(input("enter your age :"))
       if(age_<18):
        print("your too young for bank ")
       elif(age_>90):
        print("sorry, elder your old for bank")
       else:
        break
      except:
       print("only numbers ")
     while True:
      pin_=input("set a 4-digt pin  :").strip()
      if(pin_.isdigit() and len(pin_)==4):
       break
      else:
       print("pin be exsly 4-dgit")
     if(os.path.exists("data.json")):
      with open("data.json","r") as f:
       try:
        data=json.load(f)
       except:
        data={}
     else:
      data={}
     data[self.id_r] = {
            "name": name_,
            "age": age_,
            "pin": pin_,
            "bal": 0
        }
     with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

     print("Account Created Successfully!")
     print("Your Account ID:", self.id_r)

    def login(self):
     print("hello wellcome back")
     with open("data.json","r") as f:
      data=json.load(f)
     print("for exist ente exit")
     while True :
      id=input("enter your login accuont id :")
      if(id in data):
       break
      elif(id=="exit"):
       return
      else:
       print("id not exist")
     while True:
      pin_x=input("enter pin :").strip()
      if(pin_x==data[id]['pin']):
       break
      else:
       print("wrong pin")
     print("hello =======")
     while True:
      print("1.widrow money")
      print("2.dipozit")
      print("3.see balce")
      print("4.exit")
      x=input("enter :")
      if(x=="4"):
       break
      elif(x=="1"):
       try:
        wid=int(input("widrow money ? :"))
        data[id]["bal"]-=wid
        with open("data.json","w") as f:
         json.dump(data,f,indent=4)
       except:
        print("number only")
      elif(x=="2"):
       try:
        dipo=int(input("enter wid money :"))
        data[id]["bal"]+=dipo
        with open("data.json","w") as f:
         json.dump(data,f,indent=4)
       except:
        print("number only ")
      elif(x=="3"):
       print("balce:",data[id]["bal"])
      else:
       print("worng input")
    def __init__(self):
     while True:
      print("1.login")
      print("2.create")
      print("3.exit")
      x=input("enter :")
      if(x=="3"):
       break
      elif(x=="1"):
       try:
        self.login()
       except:
        print("make sure you have a account")
      elif(x=="2"):
       self.create()
      else:
       print("wrong input")



main=ATM()
