# When will the else part of try-except-else be executed? 

"""

Else Block (Jab koi error na aaye tab chalega):

else tabhi execute hota hai jab try block successfully execute ho jaye, bina kisi error ke. Matlab agar koi
exception nahi aayi, to else chalega.

✅ else ka use optional hota hai, but code readability badhata hai.

🛠 Example:

try:
    x = 10 / 2  # Yeh safe hai, koi error nahi aayegi
except ZeroDivisionError:
    print("Error: Zero se divide nahi kar sakte!")
else:
    print("Success! Division ho gaya.")  # ✅ Else chalega kyunki error nahi aayi
finally:
    print("Process complete.")  # ✅ Finally hamesha chalega

📝 Output:

Success! Division ho gaya.  
Process complete.  


"""