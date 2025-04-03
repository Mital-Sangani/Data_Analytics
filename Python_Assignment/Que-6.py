# Write a Python program to get the Fibonacci series of given range.

"""
Fibonacci series ek aisi sequence hai jisme har number pichle do numbers ka sum hota hai. Yeh series 0 se start hoti hai aur aage badhti jati hai.

Fibonacci Series Example:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Logic:

Pehle do numbers fix hote hain: 0 aur 1

Uske baad har number pichle do numbers ka sum hota hai

0 + 1 = 1

1 + 1 = 2

1 + 2 = 3

2 + 3 = 5

3 + 5 = 8 ... and so on

"""

n = int(input("Enter the range: "))
a = 0
b = 1
c = 0

for i in range(n):
    print(a, end=" ")
    c = a
    a = b
    b = c+b