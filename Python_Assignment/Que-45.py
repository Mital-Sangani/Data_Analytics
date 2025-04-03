#  Write a Python program to unzip a list of tuples into individual lists.

data = [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]

# Unzipping into individual lists
l1, l2, l3 = zip(*data)

# Converting tuples to lists (optional)
l1, l2, l3 = list(l1), list(l2), list(l3)

# Printing the results
print("List 1:", l1)
print("List 2:", l2)
print("List 3:", l3)