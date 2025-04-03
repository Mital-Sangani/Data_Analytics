# Write a python program to find the longest words.

with open("Que-78.txt", "r", encoding="utf-8") as file:
    words = file.read().split()
    
print(max(words, key=len))
