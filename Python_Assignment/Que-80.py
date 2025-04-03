# Write a Python program to count the frequency of words in a file.

# from collections import Counter

# with open("Que-80.txt", "r", encoding="utf-8") as file:
#     word_count = Counter(file.read().split())

# for word, count in word_count.items():
#     print(f"{word}: {count}")
#=====================================================================================

import json
from collections import Counter

# Load JSON data and count word frequency
with open("Que-80.json", "r", encoding="utf-8") as file:
    text = json.load(file).get("text", "")

# Print word frequencies
for word, count in Counter(text.split()).items():
    print(f"{word}: {count}")