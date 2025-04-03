# Explain Exception handling? What is an Error in Python? 
"""
Exception:

Exception ek aisa event ya condition hota hai jo program ke normal flow ko disrupt kar deta hai.

Ye tab hota hai jab program kisi error ya unexpected situation ko face karta hai at runtime.

Exceptions various situations se arise ho sakti hain, like

* Koi invalid operation perform karna

* Kisi aise resource ko access karna jo exist nahi karta

* Invalid data type ya input ka use karna

================================================================================================================

Socho, app ek website bana rahe ho aur koi user galti se invalid data enter kar de! Agar exception handle nahi 
karega, to website crash ho jayegi 😨💥.
iska solution he =>

exception handling:

Exception handling ka matlab hota hai program me hone wale errors ko expect karna aur unko manage karna,
taki program crash na ho

Agar program me koi error aa jaye, to usko smoothly handle karna zaroori hota hai, taki:

✅ Program bina crash kiye recover kar sake.
✅ Error ko skip karke agla kaam ho sake.
✅ User ko samajhne layak error message mile.

====================================================================================================

Key Concepts of Exception Handling:

1️⃣Try Block (Jisme Risky Code Hota Hai):

try block me wo code likhte hain jo error de sakta hai. Agar error aaya, to Python sidha except block me 
chala jata hai.

try:
    x = 10 / 0  # ⚠️ Risky Code

-------------------------------------------------------------------------------------------------------------------

2️⃣ Except Block (Error Handle Karne Ka Tareeka)

Agar try block me koi error aaya, to except block usko catch karta hai aur program ko crash hone se bachata hai.

except ZeroDivisionError:
    print("Error: Divide by zero not allowed!")  # 🛠️ Handle the error

-----------------------------------------------------------------------------------------------------------------

3️⃣ Else Block (Jab koi error na aaye tab chalega)

else tabhi execute hota hai jab try block successfully execute ho jaye, bina kisi error ke. Matlab agar koi
exception nahi aayi, to else chalega.

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

------------------------------------------------------------------------------------------------------------------

4️⃣ Finally Block (Hamesha Execute Hoga)

finally block hamesha run hota hai, chahe error aaye ya na aaye. Yeh useful hota hai files close karne ya 
resources free karne ke liye.

finally:
    print("This will always execute!")  # ✅ Cleanup code


---------------------------------------------------------------------------------------------------------------------

5️⃣ Raise Statement (Apni Exception Khud Raise Karna)

Agar tujhe khud se custom error dena ho, to raise ka use kar sakti hai.

age = int(input("Enter age: "))
if age < 18:
    raise ValueError("You must be at least 18 years old!")  # 🚨 Custom Error


=========================================================================================================================

🔥 Summary:

✅ try → Risky code likho
✅ except → Error handle karo
✅ else → Jab koi error na aaye tab chalo
✅ finally → Hamesha chalo (Cleanup code)
✅ raise → Apna custom error uthao

"""
#==========================================================================================================

#           ########################## ERROR #########################

"""
Error ek unexpected event hota hai jo program ke execution ke time pe hota hai. Jab program apne normal 
flow se hatke kuch galat kar leta hai, to error raise hota hai. Iska matlab hai ki program ka kuch part 
incorrectly work kar raha hai ya wo expected result return nahi kar raha hai.

Types of Errors:

1.Syntax Error

Jab code likhne mein galti hoti hai, jaise colon (:) ya parenthesis ka galat use.

Example:

if x == 5   # SyntaxError: Expected ':'
    print(x)


2.Runtime Error

Jab program chal raha ho, aur kisi unexpected situation se takra jata hai (jaise division by zero ya file na milna).

Example:

x = 10 / 0  # ZeroDivisionError

3.Logical Error

Jab code sahi syntax mein hota hai aur program run kar raha hota hai, lekin wo galat result deta hai, 
kyunki code logic mein kuch problem hoti hai.

Example:

a = 5
b = 10
print(a + b - 1)  # Expected 15, but if the logic was wrong, it could be a logical error.
In Short:
Error matlab kuch unexpected ya incorrect ho gaya program mein, jo uske normal execution ko rok leta hai.

"""


