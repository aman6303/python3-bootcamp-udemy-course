from models import Deck, Player


class Game:
    """Main game class for War card game"""

    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.round_number = 0

    def setup(self):
        """Setup the game"""
        print("\n" + "=" * 50)
        print("WAR CARD GAME")
        print("=" * 50)

        deck = Deck()
        deck.shuffle()
        hand1, hand2 = deck.split()

        self.player1.add_cards(hand1)
        self.player2.add_cards(hand2)

        print(f"\n{self.player1}")
        print(f"{self.player2}")
        print("\nLet the game begin!\n")

    def play_war(self, pot):
        """Handle war scenario"""
        print("\nWAR!")

        # Each player puts 3 cards face down
        for i in range(3):
            card1 = self.player1.play_card()
            card2 = self.player2.play_card()

            if card1 is None or card2 is None:
                return False

            pot.append(card1)
            pot.append(card2)

        # Play one card face up
        card1 = self.player1.play_card()
        card2 = self.player2.play_card()

        if card1 is None or card2 is None:
            return False

        pot.append(card1)
        pot.append(card2)

        print(f"{self.player1.name}: {card1} vs {self.player2.name}: {card2}")

        if card1.value > card2.value:
            self.player1.add_cards(pot)
            self.player1.wins += 1
            print(f"{self.player1.name} wins the war! (+{len(pot)} cards)")
        elif card2.value > card1.value:
            self.player2.add_cards(pot)
            self.player2.wins += 1
            print(f"{self.player2.name} wins the war! (+{len(pot)} cards)")
        else:
            # Another war
            return self.play_war(pot)

        return True

    def play_round(self):
        """Play one round"""
        self.round_number += 1

        card1 = self.player1.play_card()
        card2 = self.player2.play_card()

        if card1 is None or card2 is None:
            return False

        print(
            f"\nRound {self.round_number}: {self.player1.name}: {card1} vs {self.player2.name}: {card2}"
        )

        pot = [card1, card2]

        if card1.value > card2.value:
            self.player1.add_cards(pot)
            self.player1.wins += 1
            print(f"{self.player1.name} wins this round")
        elif card2.value > card1.value:
            self.player2.add_cards(pot)
            self.player2.wins += 1
            print(f"{self.player2.name} wins this round")
        else:
            # Cards are equal - WAR!
            if not self.play_war(pot):
                return False

        # Check if game should continue
        if not self.player1.has_cards() or not self.player2.has_cards():
            return False

        return True

    def show_stats(self):
        """Show final statistics"""
        print("\n" + "=" * 50)
        print("GAME OVER")
        print("=" * 50)
        print(f"\nTotal Rounds: {self.round_number}")
        print(f"\n{self.player1.name}:")
        print(f"  Cards: {self.player1.cards_count()}")
        print(f"  Rounds Won: {self.player1.wins}")
        print(f"\n{self.player2.name}:")
        print(f"  Cards: {self.player2.cards_count()}")
        print(f"  Rounds Won: {self.player2.wins}")

        if not self.player1.has_cards():
            print(f"\n{self.player2.name} WINS!")
        elif not self.player2.has_cards():
            print(f"\n{self.player1.name} WINS!")
        else:
            print("\nIt's a DRAW!")

    def play(self, max_rounds):
        """Play the complete game"""
        self.setup()

        for i in range(max_rounds):
            if not self.play_round():
                break

            # Show status every 50 rounds
            if self.round_number % 50 == 0:
                print(f"\n[Status] {self.player1} | {self.player2}")

        self.show_stats()
