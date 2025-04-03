# Write a Python program to split a list into different variables. 

data = [10, 20, 30]

a, *b, c = data

# a, *b, c = data # *(asterisk) operator ka use value ko list me lane ke liye kiya jata he

print("a:", a)
print("b:", b)
print("c:", c)