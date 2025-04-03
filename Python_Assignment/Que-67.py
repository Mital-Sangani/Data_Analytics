#  How can you pick a random item from a range? 

import random
    
# num = random.choice(range(1, 100))  # Picks a random number from 1 to 99
# print(num)

num = random.randrange(1, 100, 2)  # Picks a random odd number from 1 to 99
print(num)