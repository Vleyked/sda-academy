"""
sorted(list)
len(list)
.append(x)
.count(x)
.index(x)
.insert(index, x)
.pop(index)
.pop()
.remove(x)
.clear()
.reverse()
"""
import string


alphabet = []

alphabet += sorted(string.ascii_lowercase)

for _ in string.ascii_lowercase:  # abcdefg
    alphabet.append(_)

# string.ascii_lowercase > 'abcdefg' - letter = 'a', letter = 'b'


# alphabet = [_ for _ in string.ascii_lowercase]

# alphabet = [*string.ascii_lowercase]

print(alphabet)

# append all the letter from alphabet in the correct order
