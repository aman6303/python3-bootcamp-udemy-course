import random
from models.card import Card


class Deck:
    """Class representing a deck of cards"""

    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        """Create a standard 52-card deck"""
        suits = ["♥", "♦", "♣", "♠"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)

    def split(self):
        """Split deck into two equal halves"""
        mid = len(self.cards) // 2
        return self.cards[:mid], self.cards[mid:]
