import random


def repeated_myself():
    set_numbers = set()

    for i in range(10):
        number = random.randint(0, 100)
        # We are iterting over random numbers generated 10 times
        # Please store the number value inside the set_numbers set
        # Please maintain the same tabulation as the 7th line, otherwise it will break the code
        set_numbers.add(number)

    if len(set_numbers) < 10:
        print("Oh no I repeated myself!")

    return set_numbers


print(repeated_myself())
