#Write a program that takes a number from the user and prints the multiplication table for that number.

# #Write a program that takes a number from the user and prints whether the number is positive, negative, or zero.
# Write a program that takes two numbers from the user and prints the sum, difference, product, and quotient.
# Write a program that takes a string from the user and prints whether the string is a palindrome.

#create a vairable
#getting users input with the previous variable
#write conditional statements for those conditions
#positive, negative or zero

number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
elif number == 0:
    print("The number is zero")

#second

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print("Your answer is: ", result)

#third

string = input("Enter a sentence: ")
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("This string is not a palindrome.")

#fourth
# Write a program that takes a number from the user and prints the multiplication table for that number.

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


