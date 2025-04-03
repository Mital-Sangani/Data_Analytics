"""
✅ Explanation:

src.read() → Puri file read karta hai.

file.write() → Dusri file me likh deta hai.

Yeh sirf text files ke liye best hai.

"""


with open("Que-82.txt", "r", encoding="utf-8") as file1, open("Que-82.1.txt", "w", encoding="utf-8") as file:
    file.write(file1.read())

print("File copied successfully!")