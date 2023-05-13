"""
Let see how many string modifications techniques you know! :) 
"""


def auto_detention(sentence, number_of_repetitions):
    for i in range(number_of_repetitions):
        current_sentence = sentence
        if i % 4 == 0:
            current_sentence = current_sentence  # Please add any string modifications to current _sentence example current_sentence.upper()

        if i % 3 == 0:
            current_sentence = current_sentence  # Please add any string modifications to current _sentence example current_sentence + "!"

        print(current_sentence)


auto_detention("abc", 7)
