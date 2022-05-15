"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.generated_num = self.start -1

    def __repr__(self):
        return f"<SerialGenerator start={self.start}>"
    
    def generate(self):
        """returns the next whole number in the sequence (incrementing by 1)"""
        self.generated_num += 1
        return self.generated_num

    def reset(self):
        """resets the sequence back to the starting number inputted by the user"""
        self.generated_num = self.start -1

