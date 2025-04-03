# Write a Python program to remove duplicates from a list. 

# l1 = ["mital", "mital", "jay", "jay", "sangani", "sangani"] 

# l1 = set(l1)
# l1 = list(l1)
# print(l1)


#============================================================================================================


# without set


def func(l1):
    l2 = []
    [l2.append(i) for i in l1 if i not in l2]
    return l2

l1 = ["mital", "mital", "jay", "jay", "sangani", "sangani"] 
print(func(l1))


