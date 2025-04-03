#  Can one block of except statements handle multiple exception?

"""

✅ Haan! Ek except block multiple exceptions handle kar sakta hai.

Agar ek hi except block me multiple exceptions handle karni ho, to tuple (()) ka use karte hain.

Example 1: Handling Multiple Exceptions in One except Block

try:
    x = int("hello")  # ❌ ValueError aayegi
except (ValueError, TypeError, ZeroDivisionError):  # ✅ Multiple exceptions handled
    print("Error: Invalid operation!")

🔹 Output:

Error: Invalid operation!
✅ Yahan agar ValueError, TypeError, ya ZeroDivisionError aayegi, to wahi ek except block handle karega.

==================================================================================================================

Example 2: Handling Exception with Custom Message

try:
    lst = [1, 2, 3]
    print(lst[10])  # ❌ IndexError
except (IndexError, KeyError) as e:
    print(f"Error Occurred: {e}")  # ✅ Exception message bhi print karega
    
🔹 Output:

Error Occurred: list index out of range
✅ Yahan IndexError ya KeyError dono ek hi except block handle kar raha hai.

"""