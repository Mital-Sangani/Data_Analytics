#  Write python program that user to enter only odd numbers, else will raise an exception. 

try:
    num = int(input("Enter an odd number: "))  # User se input le rahe hain
    if num % 2 == 0:  # Even number check karenge
        raise ValueError("Only odd numbers are allowed!")  # ❌ Exception raise hoga
    print("Valid input! You entered an odd number.")  # ✅ Odd number hai, to yeh chalega
except ValueError as e:
    print(f"Error: {e}")  # ❌ Error message print hoga


"""
✔ Even number dalne pe ValueError raise ho jayega.
✔ Odd number dalne pe valid message print hoga.
✔ Agar user number ki jagah string input kare, to bhi ValueError handle ho raha hai.
✔ (except ValueError as e:) jab app number ki jagah string loge user se tab e me internally error store ho jayegi.
   matalab python khud vo error dega hame manually likhne ki jarurat nahi he. 

"""