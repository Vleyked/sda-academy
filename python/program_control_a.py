# # # Example 1: Checking if a number is positive
# num = int(input("Enter a number: "))
# if num > 0: # False
#     print("The number is positive.")
# else:
#     print("The number is not positive.")

# # # Example 2: Checking if a string is a palindrome
# string = input("Enter a string: ")
# if string == string[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("This string is not a palindrome.") 


# # LOGIC GATES
# # and --> True -> True and Ture -> only if every condition is True
# # or --> True -> True or False -> if any condition is True
# # not --> True --> False --> Only if the condition is False
# number = 1211

# if (str(number) == str(number)[::-1]) or not(type(number) == int):
#     print("Conditions met!!")
# else:
#     print("Not met!!")



# # Global scope

# a = "Visible everywhere"
# b = "Anyone can see me!!!"

# # Local scope
# if a == b:
#     print("This will only be executed when the condition is met")

# def new_func():
#     local_variable = "This variable, will only exist inside the function"
#     if type(local_variable) == str:
#         print("nested scope!!!!!")
#         if True:
#             print("Nested nested scope")
#             if True:
#                 print("Nested nested nested scope")

# new_func()

# # Example 3: Using the elif statement
num = int(input("Enter a number: "))

if num == 1: 
    print("The number is 1.")
elif num == 2:
    print("The number is 2.")
elif num == 3:  # Run
    print("The number is 3.")
else: 
    print("The number is neither 1, 2 or 3")
