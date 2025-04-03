# Write a Python script to concatenate following dictionaries to create a new one.

"""
{**dict1, **dict2, **dict3}
** (double asterisk) unpacking operator kehlata hai, jo dictionary ke key-value pairs ko nikal kar jod deta hai.

Concatenation ka matlab → Dictionaries ko jodna (merge karna).

**dict → Dictionary ke andar ke key-value pairs nikalne ke liye.

Multiple dictionaries ko aasani se jod sakte hain bina loops ke.

"""

dict1 = {'a': 100, 'b': 200}
dict2 = {'c': 300, 'd': 400}
dict3 = {'e': 500, 'f': 600}

new_dict = {**dict1, **dict2, **dict3}

print(f"Concatenated Dictionary : {new_dict}") 