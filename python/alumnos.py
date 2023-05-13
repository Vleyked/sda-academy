def ala_cats(number_of_cats):
    sentence = "Alice has 1 cat"  # Format your string here --> Example: Alice has 1 cat
    if number_of_cats == 1:
        return sentence

    else:
        sentence = f"{sentence[:9]}, {number_of_cats}"
    return print(sentence, end=" cats")


(ala_cats(3))
