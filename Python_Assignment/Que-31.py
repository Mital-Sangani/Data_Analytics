"""
Write a Python program to count the number of strings where the string  
length is 2 or more and the first and last character are same from a given list 
of strings. 

"""


l1 = ["mam", "mom", "papa", "bro", "sis"]

l2 = sum(1 for i in l1 if len(i) >= 2 and i[0] == i[-1]) 
print(l2)

