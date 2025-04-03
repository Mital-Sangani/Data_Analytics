#   How will you set the starting value in generating random numbers?

import random

random.seed(10)  # Setting the seed
print(random.randint(1, 100))  # Output will be the same every time you run this
print(random.randint(1, 100))  