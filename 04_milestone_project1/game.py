

def print_board(board):
    """Prints the current state of the board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    """Checks if the given player has won."""
    # Winning combinations (rows, columns, diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Cols
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_full(board):
    """Checks if the board is full (Draw condition)."""
    return " " not in board

def want_to_continue():
    
    while True:
        choice = input("Do you want to continue (Y) ?").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid Input! Please enter y or n!!")
        

def tic_tac_toe():
    """Main game function."""
    # Initialize empty board
    board = [" "] * 9
    current_player = "X"
    game_running = True

    print("Welcome to Tic-Tac-Toe!")
    print("Use numbers 1-9 to place your move.")
    print_board([str(i+1) for i in range(9)]) # Show position guide
    print("Let's start!\n")

    while game_running:
        print_board(board)
        try:
            # Get user input (subtract 1 to match 0-8 index)
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
            
            # Validation
            if move < 0 or move > 8:
                print("Invalid input! Please choose a number between 1 and 9.")
                continue
            if board[move] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Make the move
            board[move] = current_player

            # Check Win
            if check_winner(board, current_player):
                print_board(board)
                print(f" Player {current_player} wins! ")
                game_running = False
            
            # Check Draw
            elif is_full(board):
                print_board(board)
                print("It's a Draw! ")
                game_running = False
            
            # Switch Player
            else:
                current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number.")
            
def main():
    while True:
        tic_tac_toe()
        if not want_to_continue():
            break


if __name__ == "__main__":
    main()