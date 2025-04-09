age = int(input("Enter your age : "))
week = input("Enter your weekday : ")


if age > 0 and age <= 12 :
    base_price = 5
    print(f"Base price : {base_price}")
    if week == "Saturday" or week == "Sunday" or week == "saturday" or week == "sunday":
        Final = base_price * 0.10
        Final_price = base_price - Final
        print("Discount : 10%")
        print(f"Final price : {Final_price}")
elif age >= 13 and age <= 17 :
    base_price = 8
    print(f"Base price : {base_price}")
    if week == "Saturday" or week == "Sunday" or week == "saturday" or week == "sunday":
        Final = base_price * 0.10
        Final_price = base_price - Final
        print("Discount : 10%")
        print(f"Final price : {Final_price}")
elif age >= 18 and age <= 64 :
    base_price = 12
    print(f"Base price : {base_price}")
    if week == "Saturday" or week == "Sunday" or week == "saturday" or week == "sunday":
        Final = base_price * 0.10
        Final_price = base_price - Final
        print("Discount : 10%")
        print(f"Final price : {Final_price}")
else : 
    base_price = 7
    print(f"Base price : {base_price}")
    if week == "Saturday" or week == "Sunday" or week == "saturday" or week == "sunday":
        Final = base_price * 0.10
        Final_price = base_price - Final
        print("Discount : 10%")
        print(f"Final price : {Final_price}")