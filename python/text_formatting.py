# Print function, prints something in the terminal.
# print("Hello", 123, "World")
# print(False, 123, "World")
# print(hex(1235), "Hello", bin(1234))
# print("Hello", "\n", "World", "!", sep=" ")


# Formatting text
# Several ways

# 1st f interpolation
# a = "World"
# b = "Hello"
# c = "Jhon"

# print(f"{b} {a}, My name is {c}!")  # Newer and faster.
# print("Hello {}!".format(a))  # Kind of new but slower.
# print("Hello %s!" % a)  # Oldest one, faster than format but hard to read.

#### formatting numbers
# Format float values
# n = 3.2334535464564574656
# print(f"This is my rounded number! {n: .5f}")

# n_percent = 0.75
# print(f"This is my rounded number! {n_percent: .1%}")

# a = "This is an example of a large string"
# b = "kkjdhfk skdjhfalkjf lskhd k z"
# c = "Hello World!"

# print(c.index("World"))

# print("hello".capitalize())

# print(my_function(500, 500))

# Symbols use cases
# ()
# 1. Calls a function or class, Entering, parameters into a function.
def my_function(number_a, number_b):
    result = number_a + number_b
    return result


print(my_function(500, 500))

# 2. Isolate operations
calculation = 3 + 5 * 10 / 2
calculation = (3 + 5) * (10 / 2)

# 3. Starting tuples
a = ()

# {}
# 1. Syntax to format a string
a = "Jhon"
print(f"Hello my name is {a}")

# 2. Start a diccionary
a = {}

# []
# 1. Is used to access index of a collection
a = "Hello world"
a[1]  # e
# 2. Start list
a = [1, 2, 3, 4]


calculation = (3 + 5) * (10 / 2)
print(calculation)
