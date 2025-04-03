# Write a python program to sum of the first n positive integers.

p_sum = 0
for i in range(1,6):
    num = int(input("Enter the number : "))
    if num > 0:
        print("positive")
        p_sum += num
    else:
        print("negative")
print(f"sum of positive number is : {p_sum}")