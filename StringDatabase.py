import random


class StringDatabase:
    def __init__(self, filename):
        self.words = self.load_words(filename)

    # Read and add words to a list
    def load_words(self, filename):
        with open(filename, 'r') as file:
            return [word.strip() for line in file for word in line.split()]

    # Generate (random) word from list
    def random_word(self):
        return random.choice(self.words)
