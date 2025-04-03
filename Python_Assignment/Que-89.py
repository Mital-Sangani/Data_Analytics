# How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets. 

"""

✅ try → Risky code likho
✅ except → Error handle karo
✅ finally → Hamesha chalega (Cleanup code)

==============================================================================================================

Example : 1

try:
    x = 10 / 0  # ❌ ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")  
finally:
    print("This will always execute.")  # ✅ Finally block hamesha chalega

output:
Error: Cannot divide by zero!
This will always execute.

====================================================================================================================

Example : 2 (Handling Multiple Exceptions)

try:
    num = int(input("Enter a number: "))  # ❌ ValueError agar string input karein
    result = 10 / num  # ❌ ZeroDivisionError agar 0 input karein
    print("Result:", result)
except ValueError:
    print("Error: Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("Execution completed.")


    🔹 Possible Outputs:

✅ Case 1: User inputs "hello"

Error: Invalid input! Please enter a number.
Execution completed.

✅ Case 2: User inputs 0

Error: Cannot divide by zero!
Execution completed.

✅ Case 3: User inputs 5

Result: 2.0
Execution completed.

✅ Har case me finally block execute ho raha hai! 



"""