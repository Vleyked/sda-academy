# Dictionaries

a = [1, 2, 3, 4]

phonebook = {"Jhon": 675543323, "Anne": 465382948, "Frank": 443382948}

# del phonebook["Jhon"]

name = "Jhon"

number = phonebook.get(name, "The value doesn't exist")

print(f"Calling {name}, number: {number}")
