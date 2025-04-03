"""

Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.
 
"""


str1 = input("Enter first string: ")  
str2 = input("Enter second string: ")  

if len(str1) >= 2 and len(str2) >= 2:  
    string1 = str2[:2] + str1[2:]  
    string2 = str1[:2] + str2[2:]  
    string = string1 + " " + string2 
    print("Result:", string)  
else:  
    print("Both strings must have at least two characters!")  