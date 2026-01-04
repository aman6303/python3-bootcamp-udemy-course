class Card:
    """Class representing a playing card"""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.get_value()

    def get_value(self):
        """Get numerical value of card"""
        if self.rank == "A":
            return 14
        elif self.rank == "K":
            return 13
        elif self.rank == "Q":
            return 12
        elif self.rank == "J":
            return 11
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"
