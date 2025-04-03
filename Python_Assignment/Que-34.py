# Write a Python function that takes two lists and returns true if they have at least one common member.

def func(l1,l2):
    
    for i in l1:
        if i in l2:
            return True
    return False
        
l1 = [1,2,3,4,5]
l2 = [7,8,9,3,10]

print(func(l1,l2))