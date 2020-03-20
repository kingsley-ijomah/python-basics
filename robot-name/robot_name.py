from string import ascii_uppercase, digits
from random import seed, sample

class Robot:
    def __init__(self):
        self.generate_name()

    def generate_name(self):
        seed()
        self.name = self.alphabets() + self.digits()

    def reset(self):
        self.generate_name()

    @staticmethod
    def alphabets():
        return "".join(sample(ascii_uppercase, 2))

    @staticmethod
    def digits():
        return "".join(sample(digits, 3))

