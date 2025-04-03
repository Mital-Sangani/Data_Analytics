#  Write a Python function to check whether a number is perfect or not.

"""
Example of Perfect Numbers:
6 → Divisors: 1, 2, 3 → 1 + 2 + 3 = 6 ✅
28 → Divisors: 1, 2, 4, 7, 14 → 1 + 2 + 4 + 7 + 14 = 28 ✅
496 → Divisors: 1, 2, 4, 8, 16, 31, 62, 124, 248 → Sum = 496 ✅

"""
def func():
    num = int(input("Enter a number : "))
    return sum(i for i in range(1,num) if num % i == 0) == num
print(func())
    