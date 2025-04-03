# Write a Python program to count the number of lines in a text file.

count = 0
with open("Que-74.txt", "r", encoding="utf-8") as file:
    for i in file:  
        count += 1

print("Total number of lines:", count)