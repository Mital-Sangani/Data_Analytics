#  Write a Python program to check whether a list contains a sub list 


main_list = [1, 2, 3, 4, 5, 6]
sub_list = [1]

status = True
for i in sub_list:
    if i not in main_list:
        status = False
        break
    status = True

print(status)  


#================ set ki method issubset() ka use karke ==========================================

# def func(main_list, sub_list):
#     return set(sub_list).issubset(set(main_list))

# print(func([1, 2, 3, 4, 5], [2, 3]))   
# print(func([1, 2, 3, 4, 5], [3, 5]))  
# print(func([1, 2, 3, 4, 5], [6, 7]))   