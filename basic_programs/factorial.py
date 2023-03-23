# Using built_in fn

import math
num = int(input("Enter no:"))
fact = math.factorial(num)
print(f'The factorial of {num} is {fact}.')

# Using recurssive method

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
    
num =int(input('Enter a no:'))
print(f'The factorial of the {num} is {factorial(num)}')
