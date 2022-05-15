"""Special Word Finder: finds random words from a dictionary. Ommits blank lines and comments"""
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)
    
    def get_words(self):
        """returns the list of words generated from the inputted file path. Ommits blank lines and comments"""
        file = open(self.path, 'r')
        words = [ line[:-1] for line in file if line.strip() and not line.startswith('#')]
        file.close()
        return words