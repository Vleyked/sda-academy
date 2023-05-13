# Everything in this file is an object
# The function is an object
def function():
    pass


print(function.__class__)

# The variable is an object
variable = 1
print(variable.__class__)

# The class is an object
class Class:
    pass


print(Class.__class__)

# The module, package, library is an object
import os

print(os.__class__)

# Any data type is an object
# Task: Create variables for each data type and print their class
# Example
# integer = 1
# print(integer.__class__)
