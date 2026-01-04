from game import Game


def get_player_names():
    """Get player names from user"""
    print("\nWelcome to Card War!")

    name1 = input("\nEnter Player 1 name: ").strip()
    if name1 == "":
        name1 = "Player 1"

    name2 = input("Enter Player 2 name: ").strip()
    if name2 == "":
        name2 = "Player 2"

    return name1, name2


def get_round_limit():
    """Get maximum rounds from user"""
    rounds = input("\nHow many rounds to play? (default 1000): ").strip()
    if rounds == "":
        return 1000
    else:
        try:
            return int(rounds)
        except ValueError:
            print("Invalid input. Using default 1000 rounds.")
            return 1000


def main():
    """Main entry point"""
    name1, name2 = get_player_names()
    max_rounds = get_round_limit()

    game = Game(name1, name2)
    game.play(max_rounds)


if __name__ == "__main__":
    main()
