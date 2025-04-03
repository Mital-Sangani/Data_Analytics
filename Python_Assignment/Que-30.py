# How will you compare two lists?

"""
1. Use == → If order and elements must be the same.

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  

2. Use sorted(list1) == sorted(list2) → If order doesn't matter but elements must match.

list1 = [1, 2, 3]
list2 = [3, 1, 2]

print(sorted(list1) == sorted(list2))  # Output: True

3. Use set(list1) == set(list2) → If duplicates don't matter.

list1 = [1, 2, 3, 3]
list2 = [3, 1, 2]

print(set(list1) == set(list2))  # Output: True

4. Use set(list1) - set(list2) → To find differences.

list1 = [1, 2, 3, 4]
list2 = [1, 2, 5]

print(set(list1) - set(list2))  # Output: {3, 4} (Elements in list1 but not in list2)
print(set(list2) - set(list1))  # Output: {5} (Elements in list2 but not in list1)

5. Use issubset() → To check if one list is inside another.

list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]

print(set(list1).issubset(set(list2)))  # Output: True


"""

