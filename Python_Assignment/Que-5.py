#  Write a Python program to get the Factorial number of given numbers.


n = 1
num = int(input("Enter the number : "))

for i in range(1,num+1):
    n *= i

print(n)