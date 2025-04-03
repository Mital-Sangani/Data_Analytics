# When is the finally block executed? 

"""
✅ finally block hamesha execute hota hai, chahe exception aaye ya na aaye.
✅ Agar try block me error aaye ya except block chale, finally block fir bhi execute hoga.
✅ Iska use cleanup operations (like closing files, releasing resources, etc.) ke liye hota hai.

================================================================================================================

Example 1: No Error (Finally still executes)

try:
    print("Try block executing...")
except:
    print("Exception occurred!")
finally:
    print("Finally block executing!")  # ✅ Hamesha chalega

🔹 Output:

Try block executing...
Finally block executing!
✅ Yahan koi error nahi aayi, but finally fir bhi execute ho gaya.

================================================================================================================

Example 2: Error Occurs (Finally still executes)

try:
    x = 10 / 0  # ❌ ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Cleanup done!")  # ✅ Hamesha chalega

🔹 Output:

Cannot divide by zero!
Cleanup done!

✅ Yahan except block chala, lekin finally fir bhi execute ho gaya.




"""