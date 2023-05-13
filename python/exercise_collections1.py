# Task 1: Random euromillion valid nubers
# For this task you will need to use the random library to return a valid euromillion numbers
# numbers --> 5 numbers, range(1-50)
# stars --> 2 numbers, rango(1-12)
# The numbers cannot be repeated

# Expected output
# [2, 9, 34, 50, 34], [2, 7]

# Invalid output
# [2, 5, 34], [3] -> Less numbers than needed
# [0, 23, 43, 32, 55] [3, 21] --> numbers out of range
# [23, 23, 43, 43, 55] [5, 11] --> numbers repeated


import random


def random_euromillion():
    # Your code here!!
    # Generating numbers
    numbers = set()
    while len(numbers) < 5:
        numbers.add(random.randint(1, 50))

    # Generating stars
    stars = set()
    while len(stars) < 2:
        stars.add(random.randint(1, 12))
        
    return list(numbers), list(stars)

print(random_euromillion())






def random_euromillions():
    numbers = list(set([rnd(range(51)) for i in range(5)]))
    stars = list(set([rnd(range(13)) for i in range(2)]))

    if len(numbers) < 5 or len(stars) < 2:
        return random_euromillions()

    return numbers, stars



# import random
# def random_euromillion():
#     first_list = []
#     second_list = []
#     while len(first_list) < 5:
#         first_list = []
#         first_list += set(random.randint(1, 50) for x in range(5))
#     while len(second_list) < 2:
#         second_list = []
#         second_list += set(random.randint(1, 12) for x in range(2))
#     return first_list, second_list

print(random_euromillion())



# for n in range(1000):
#     new_number = random_euromillion()
#     if len(set(new_number[0])) != 5:
#         print("BAAAAD")
