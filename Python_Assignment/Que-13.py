# Write a Python program that will return true if the two given integer values are equal.


# num1 = int(input("Enter the number : "))
# num2 = int(input("Enter the number : "))

# if num1 == num2:
#     print("true")
# else:
#     print("false")


#=============================================================================================


def func(num1,num2):
    if num1 == num2:
        return "true"
    else:
        return "false"

num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))

print(func(num1,num2))

