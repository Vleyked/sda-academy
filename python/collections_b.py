# # Diccioaries, list, tuples, and sets

# custom_tuple = (1, 2, 3)

# dictionary = {"a": 1, "b": 2, "c": 3}
# custom_list = [1, 2, 3, 4, 5, 6, 7]
# custom_set = {1, 2, 3}


# ############################ LIST ##########################
# # Modifying a list
# custom_list.append(3)
# custom_list.pop()
# custom_list.insert(0, 3)
# custom_list.pop(0)
# custom_list = custom_list[1:4]

# # Read list
# custom_list
# custom_list[1]

# # Example 1: Creating a list of numbers
# numbers = [1, 2, 3, 4, 5]

# # Example 2: Creating a list of strings
# names = ["John", "Jane", "Jim", "Jill"]

# # Example 3: Creating a list of mixed data types
# mixed = [1, "John", 3.14, True]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]

print(numbers[1:8:1]) # [2,3,4, 5, 6, 7, 8]
print(numbers[1:8:2]) # [2, 4, 6, 8]
print(numbers[1:8:3]) # [2, 5, 8]



############################ DICT ##########################
# Example 1: Creating a dictionary of numbers
numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

# Example 2: Creating a dictionary of strings
names = {"John": 28, "Jane": 32, "Jim": 35, "Jill": 25}

# Example 3: Creating a dictionary of mixed data types
mixed = {1: "one", "John": 28, 3.14: "pi", True: "yes"}


# Modifying a dict
dictionary["d"] = 4
dictionary["e"] = 5
# dictionary.clear()

# Read dict
dictionary["a"]
dictionary.get("a")


############################ SET ##########################
# Modifying a dict
custom_set.add(4)
custom_set.add(3)
custom_set.remove(3)

# Special operations
custom_set1 = {1, 2, 3}
custom_set2 = {3, 4, 5}
custom_set1.difference(custom_set2)
custom_set1.intersection(custom_set2)

# Read
# print(1 in custom_set)

# Example 1: Creating a set of numbers
numbers = {1, 2, 3, 4, 5}

# Example 2: Creating a set of strings
names = {"John", "Jane", "Jim", "Jill"}

# Example 3: Creating a set of mixed data types
mixed = {1, "John", 3.14, True}


############################ TUPLE ##########################
# Only read
one_element = (1)
a = (1, 2, 3, 4)
print(a[0])


a = [
    1,
    2,
    3,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    6,
]  # Good for modifying values inside if you want to preserve sort order
unique_values = set(a)  # Good for reading values efficiently and store unique values
b = {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 6}
