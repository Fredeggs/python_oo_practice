"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    def __init__(self, path):
        self.path = path
        self.words = self.get_words()
        print(self.num_words())
    
    def num_words(self):
        """returns a string that displays the number of words in the file"""
        count = 0
        for word in self.words:
            count += 1
        return f"{count} words read"
    
    def get_words(self):
        """returns the list of words generated from the inputted file path"""
        file = open(self.path, 'r')
        words = [ line[:-1] for line in file ]
        file.close()
        return words

    def random(self):
        """returns a random word from the word list generated from the file path"""
        return choice(self.words)
