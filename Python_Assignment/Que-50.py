# Write a Python script to check if a given key already exists in a dictionary. 


d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

key_to_check = 'b'

if key_to_check in d1:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")