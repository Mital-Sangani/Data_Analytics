#  Write a Python function that checks whether a passed string is palindrome or not

# Examples of Palindrome strings:
# ✅ mom → Reverse = mom (Same)
# ✅ dad → Reverse = dad (Same)
# ✅ madam → Reverse = madam (Same)
# ❌ moon → Reverse = noom (Not Same)

def func():
    num = input("Enter a number : ")

    return num == num[::-1]

print(func())