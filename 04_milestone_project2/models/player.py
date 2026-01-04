class Player:
    """Class representing a player"""

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.wins = 0

    def add_cards(self, cards):
        """Add cards to player's hand"""
        self.hand.extend(cards)

    def play_card(self):
        """Play the top card"""
        if len(self.hand) > 0:
            return self.hand.pop(0)
        return None

    def has_cards(self):
        """Check if player has cards"""
        return len(self.hand) > 0

    def cards_count(self):
        """Return number of cards"""
        return len(self.hand)

    def __str__(self):
        return f"{self.name}: {self.cards_count()} cards"
