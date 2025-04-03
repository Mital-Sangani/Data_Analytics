#  Write a Python program to read a file line by line and store it into a list 

with open("Que-74.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # Read lines into a list

print(lines)