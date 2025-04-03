# How Do You Check the Presence of a Key in A Dictionary?

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

key_to_check = 'b'

if key_to_check in d1:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")