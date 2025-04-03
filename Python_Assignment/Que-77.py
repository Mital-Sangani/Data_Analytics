# Write a Python program to read a file line by line store it into a variable.

with open("Que-74.txt", "r", encoding="utf-8") as file:
    content = file.read()  # Read entire file into a variable

print(content)

