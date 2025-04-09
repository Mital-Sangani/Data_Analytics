
                             ################# manager site ################## 

site = input("choose any one : Manager ya Customer : ")

if site == "Manager":

    products = {} # mainDictionary 

    status = True 

    while status:
        specification = {} # sub Dictionary 
        
        product_name = input("Enter product name : ")
        product_qty = int(input("Enter qty : "))
        product_price = int(input("Enter product price : "))

        if product_name in products.keys():
            specification["qty"] = products[product_name]["qty"] + product_qty
            specification["price"] = product_price

        else:
            specification["qty"] = product_qty
            specification["price"] = product_price

        products[product_name] = specification

        for k in products.keys():
            print(f"{k}  | Qty. {products[k]["qty"]}  | Price (1 pc): Rs. {products[k]["price"]} ")

        choice = input("Do you want to enter more product ? press 'y' for yes and press 'n' for no : ")
        if choice == 'y' or choice == 'yes':
            status = True 
        else:
            status = False

else:
    

                       ################# customer site ################## 
    products = {
            "menu" : { 
                "Pizza": {"price": 200, "stock": 5},
                "Burger": {"price": 100, "stock": 10},
                "Pasta": {"price": 150, "stock": 3},
                "Salad": {"price": 80, "stock": 7},
                "Ice Cream": {"price": 50, "stock": 0}
            },

            "orders": []
    }
    print("\n------------- Menu -------------"),print()

    for item, details in products["menu"].items():
         print(f"{item} - Price: {details['price']} Rs, Stock: {details['stock']}")
    
    status = True
    total = 0
    while status:
        
        print()
        product_name = input("What you want to eat ?? : ")
    
        if product_name in products['menu']:

            price_per_item = products['menu'][product_name]["price"]
            available_stock = products['menu'][product_name]['stock']
            print(f"Per pc price is : {price_per_item} Rs")
            print(f"Available stock is : {available_stock} ")
            print()

            qty = int(input("Enter qty do you want ? : "))

            if qty <= available_stock:
                product_price = price_per_item * qty
                print(f"Total: {price_per_item} X {qty} = {product_price} Rs")
                print()
                choice = input("do you want to proceed it ? press 'y' for yes and press 'n' for no : ")
                if choice == 'y' or choice == 'yes':
                    products['orders'].append({
                        'product': product_name,
                        'quantity': qty,
                        'total_price': product_price
                    })
                    total += product_price
                    print("------ Your order has been placed successfully! ------")
                    print()
                else:
                    print("Order canceled.")
            else:
                print("sorry !!!! This item is out of stock")
        else:
            print("Sorry, this product is not available in the menu.")
        
        order = input("Do you want more item ? press 'y' for yes and press 'n' for no : ")
        if order == "n":
            status = False
            print()
            print(f"Your total bill amount : {total}Rs.")
            print()
            print("🙏🙏🙏😊😊 Thank you For visite our restaurent 😊😊🙏🙏🙏")
            print()
        else :
            status 



    



        