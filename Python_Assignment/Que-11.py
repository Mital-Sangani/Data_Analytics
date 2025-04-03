#  Write a Python program to test whether a passed letter is a vowel or not

# char = input("Enter the charactor : ")

# if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#     print("vowel")
# else:
#     print("not vowel")


#==================================================================================


# charactor = input("Enter the charactor :")

# if charactor in "aeiou":
#     print("vowel")
# else:
#     print("not vowel")

#==========================================================================================

charactor = input("Enter the charactor :")
char = "aeiou"

for i in char:
    if i == charactor:
        print("vowel")
    else:
        print("Not vowel")    