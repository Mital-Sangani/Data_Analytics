# Write a Python program to generate and print a list of first and last 5 elements where the values
#  are square of numbers between 1 and 30.

l1 = [i**2 for i in range(1,31)]
print(l1)
print(f"Fisrt Five Elements : {l1[:5]}")
print(f"Fisrt Five Elements : {l1[-5:]}")



