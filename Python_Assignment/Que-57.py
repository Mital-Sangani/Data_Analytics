#  Write a Python program to find the highest 3 values in a dictionary 

d = {'a': 200, 'b': 120, 'c': 80, 'd': 20, 'e': 90, 'f': 140}

d1 = list(d.values())

print(d1)

max1 = max(d1)
d1.remove(max1)

max2 = max(d1)
d1.remove(max2)

max3 = max(d1)

print(max1,max2,max3)