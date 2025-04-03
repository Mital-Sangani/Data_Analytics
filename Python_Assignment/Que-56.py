# Write a Python program to map two lists into a dictionary 
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

from collections import Counter

keys = ['a', 'b', 'c', 'd']
values = [400, 400, 300, 400]

d = Counter(dict(zip(keys, values)))
print("Counter Output:", d)


"""
what is counter ?

it is part of collection modules
it is subclass of dict(dictionary)
kisi bhi list, tuple ya string ke elements ko count kar sakta hai.

========================================================================================
🔹 Why Use Counter?

✔ Auto-counting: No need for loops to count elements.
✔ Handles missing keys: No KeyError, default count is 0.
✔ Faster & optimized: Works better than a regular dictionary for counting.
=======================================================================================

✅ Counter Handles Missing Keys (No KeyError, Default Count = 0)

Regular Dictionary (Gives KeyError)

normal_dict = {}
print(normal_dict['apple'])  # ❌ KeyError: 'apple'

===================================================================================

Counter (No KeyError, Default Count = 0)

from collections import Counter

count = Counter()  # Empty Counter

print(count['apple'])  # ✅ Output: 0 (No error)


"""

