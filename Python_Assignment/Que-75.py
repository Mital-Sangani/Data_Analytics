# Write a Python program to read last n lines of a file. 

def read_Last_n_lines(filename, n):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()  # File ki saari lines ek list me store karenge
        print("".join(lines[-n:]))  # Last `n` lines print karenge

read_Last_n_lines("Que-74.txt", 3)

