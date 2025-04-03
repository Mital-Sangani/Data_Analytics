
#  Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.

from collections import Counter

s = "w3resource"
d = dict(Counter(s))  
print(d)


#=====================================================================================================

s = "w3resource"
d = {}

for char in s:
    d[char] = d.get(char, 0) + 1  # Agar char pehle se hai toh +1, warna 0 se start
print(d)