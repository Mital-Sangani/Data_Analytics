# Write python program that swap two number with temp variable and without temp variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swapping: a =", a, ", b =", b)
