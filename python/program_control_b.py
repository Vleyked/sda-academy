# number = 1
# while number != 10: # This condition will be true when the i value is 10 or more
#     print(number)
#     number = number + 1 # number = 1 + 1 --> number = 2 --> number = 2 + 1 --> number = 3 --> number = 3 + 1 --> number = 4

# print("While loop finished!!! yeeey!")


# fruits = ["apple", "banana", "cherry", "date"]
# for iterator in fruits: # iterator = cherry
#     if iterator == "cherry":
#         continue # This keywork stops the execution and continue to the next iteration
#     print(iterator)

# """
# apple
# banana
# date
# """

# def custom_enumerate(collection):
#     return [n for n in range(len(collection))], collection

fruits = ["orange", "banana", "cherry", "date"]

fruits_modified = []
for fruit in fruits:
    fruits_modified.append(fruit.upper())

fruits_modified_list_comprehension = [fruit.upper() for fruit in fruits]

print(fruits_modified_list_comprehension)
    





print(enumerate(fruits))
