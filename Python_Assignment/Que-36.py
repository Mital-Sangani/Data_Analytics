# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_elements(lst):
    return list(set(lst))  # Set se duplicates remove, list me convert

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  
print(unique_elements(["apple", "banana", "apple", "cherry"]))