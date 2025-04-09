from datetime import *

d = datetime.now()
f = open(f"{d.strftime("%m%d%Y")}.txt","a")

company = "-----------------KALYAN JWELLERS------------------"
thankyou = "------------------- THANK YOU --------------------"
name = input("Enter your name : ")
gender = input("Enter your gender : ")
age = int(input("Enter your age : "))
product = input("Enter your product : ")
product1 = []
product1.append(product)
pro_gram = int(input("Enter your product in gram : "))
current_gold_price = 5752
status = True
while status :
    choise = input("Do you want more product ?? 'y' for yes and 'n' for no : ")

    if choise == 'y' or choise == 'yes':
        product = input("Enter your product : ")
        product1.append(product)
        program = int(input("Enter your product in gram : "))
        pro_gram += program
    else:
        status = False

total_gold_rate = current_gold_price * pro_gram
Making_charges = 845
Total_Making_Charges = pro_gram * Making_charges
Total_Amount = total_gold_rate + Total_Making_Charges
discount = 0
print(" ")

if gender == "male" or gender == "Male":
    if age > 65 :
        if Total_Amount > 21000 and Total_Amount < 31000:
            discount = Total_Amount * 20/100
            d = 20
        elif Total_Amount > 31000 and Total_Amount < 51000:
            discount = Total_Amount * 30/100
            d = 30
        elif Total_Amount > 51000:
            discount = Total_Amount * 35/100
            d = 35
    else:
        if Total_Amount > 21000 and Total_Amount < 31000:
            discount = Total_Amount * 10/100
            d = 10
        elif Total_Amount > 31000 and Total_Amount < 51000:
            discount = Total_Amount * 20/100
            d = 20
        elif Total_Amount > 51000:
            discount = Total_Amount * 25/100
            d = 25
    f.write(f"{company} \nName : {name} \nGender : {gender} \nAge : {age} \nProduct : {product1} \nProduct(gram) : {pro_gram} \n------------------------------------------------- \nCurrent Gold Rate is : {current_gold_price} \n------------------------------------------------- \nTotal gold rate is : {total_gold_rate} \n\n")
    f.write(f"Making Charges is : {Making_charges}/g \nTotal Making Charges is : {Total_Making_Charges} \n-------------------------------------------------- \nTotal Amount is : {Total_Amount} \n-------------------------------------------------- \nYour Discount is : {d}% \nYour Discount amount is : {discount} \n-------------------------------------------------- \nYour Net amount : {Total_Amount - discount} \n-------------------------------------------------- \n\n")
    
elif gender == "female" or gender == "Female":
    if age > 65 :

        if Total_Amount > 21000 and Total_Amount < 31000:
            discount = Total_Amount * 25/100
            d = 25
        elif Total_Amount > 31000 and Total_Amount < 51000:
            discount = Total_Amount * 35/100
            d = 35
        elif Total_Amount > 51000:
            discount = Total_Amount * 40/100
            d = 40
    else:
        if Total_Amount > 21000 and Total_Amount < 31000:
            discount = Total_Amount * 15/100
            d = 15
        elif Total_Amount > 31000 and Total_Amount < 51000:
            discount = Total_Amount * 25/100
            d = 25
        elif Total_Amount > 51000:
            discount = Total_Amount * 30/100
            d = 30
    f.write(f"{company} \nName : {name} \nGender : {gender} \nAge : {age} \nProduct : {product1} \nProduct(gram) : {pro_gram} \n------------------------------------------------- \nCurrent Gold Rate is : {current_gold_price} \n------------------------------------------------- \nTotal gold rate is : {total_gold_rate} \n\n")
    f.write(f"Making Charges is : {Making_charges}/g \nTotal Making Charges is : {Total_Making_Charges} \n-------------------------------------------------- \nTotal Amount is : {Total_Amount} \n-------------------------------------------------- \nYour Discount is : {d}% \nYour Discount amount is : {discount} \n-------------------------------------------------- \nYour Net amount : {Total_Amount - discount} \n-------------------------------------------------- \n\n")
        
else:
    d = 0
    total_gold_rate = 0
    Total_Making_Charges = 0
    Total_Amount = 0
    Making_charges = 0
    discount = 0
    company = "#####--- Your gender is invalid ---#####"
    thankyou = "#####--- Your gender is invalid ---#####"

print(company),print(" ")
print(f"Name : {name}")
print(f"Gender : {gender}")
print(f"Age : {age}")
print(f"Product : {product1}")
print(f"Product(gram) : {pro_gram}")
print("-------------------------------------------------")
print(f"Current Gold Rate is : {current_gold_price}")
print("-------------------------------------------------")
print(f"Total gold rate is : {total_gold_rate}")
print(" ")
print(f"Making Charges is : {Making_charges}/g")
print(f"Total Making Charges is : {Total_Making_Charges}")
print("--------------------------------------------------")
print(f"Total Amount is : {Total_Amount}")
print("--------------------------------------------------")
print(f"Your Discount is : {d}%")
print(f"Your Discount amount is : {discount}")
print("--------------------------------------------------")
print(f"Your Net amount : {Total_Amount - discount}")   
print("--------------------------------------------------")  
print(thankyou) 

  