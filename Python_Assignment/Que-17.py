# What are negative indexes and why are they used? 

"""
defination:

Python me negative indexes ka use sequence ke end se elements access karne ke liye hota hai. 
Yeh lists, tuples aur strings ke saath kaam karta hai.

✅ Last element ka index -1 hota hai
✅ Second-last element ka index -2 hota hai, aur aise hi aage badhta hai

=======================================================================================================================

example in string :

text = "Python"
print(text[-1])  # Output: 'n'
print(text[-3])  # Output: 'h'

========================================================================================================================

Why Are Negative Indexes Used?

🔹 Sequence ke end se access karna easy ho jata hai: len(list) - 1 calculate karne ki zaroorat nahi.

🔹 Errors avoid karne me madad karta hai: Jab list ka size dynamic ho, tab negative indexing kaafi useful hoti hai.

🔹 Slicing me kaam aata hai: Jab list ya string ke last ke kuch elements extract karne ho.

Matlab negative indexing ek shortcut hai jo coding ko aur easy aur clean banata hai
"""