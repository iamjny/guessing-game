import random


class StringDatabase:
    pass


with open('four_letters.txt', 'r') as file:
    words = [word.strip() for line in file for word in line.split()]


def random_word(words_list):
    return random.choice(words_list)
