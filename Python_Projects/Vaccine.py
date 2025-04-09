from datetime import *

d = datetime.now()
f = open(f"{d.strftime("%m%d%Y")}.txt","a")
try:
    name = input("Enter Your name : ")
    Email = input("Enter your Email : ")
    age = int(input("Enter Your age : "))
    gender = input("Enter your Gender(male/female) : ")
    vaccine = input("Enter Your vaccine name : ")
    vaccine_doze = int(input("Enter Your vaccine doze : "))
    f.write(f"\nVACCINATION REPORT : \n====================================================\nDATE : {d.date()}             time : {d.time()}")
    f.write(f"\n----------------------------------------------------\nNAME : {name}\nEMAIL : {Email}\nAGE : {age}\nGENDER : {gender}\nVACCINE : {vaccine}\nVACCINE DOZE : {vaccine_doze}")
    f.write("\n")
    f.close()
    
    print("File created succesfully ")
except :
    print("invalide data ")