# Write a Python program to write a list to a file. 


my_list = ["Apple\n", "Banana\n", "Cherry\n", "Mango\n"]

# File me list ko write karna
with open("Que-81.txt", "w", encoding="utf-8") as file:
    file.writelines(my_list)

print("List saved successfully!")