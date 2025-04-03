# Write a Python function to check whether a number is in a given range


def func():
    num = int(input("Enter the number : "))
    start = int(input("Enter the starting number : "))
    end = int(input("Enter the endig number : "))

    if start <= num <= end:
        return True
    else:
        return False
    
print(func()) 