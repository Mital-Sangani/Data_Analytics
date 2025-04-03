# Write a Python program to count the occurrences of each word in a given sentence.

string = input("Enter the sentence : ")
words = string.split()
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1 
    else:
        words_count[word] = 1

print(f"{words_count}")