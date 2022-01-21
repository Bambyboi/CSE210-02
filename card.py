import random

class Card:
    def __init__(self):
      #cards points
        self.cards = 0
        self.points = 300

    def pick(self):
        self.cards = random.randint(1, 13)
