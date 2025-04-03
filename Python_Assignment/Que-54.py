#  Write a Python program to check multiple keys exists in a dictionary

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys = ['a', 'c']

for k in keys:
    if k in d:
        print("All keys exist")
    else:
        print("Some keys are missing")