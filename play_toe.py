from src import deftoe


def main():
    """
    Main function to run the Tic Tac Toe game.
    
    This function initializes the game board, manages player turns, and handles
    the game loop, including win/draw detection and prompting for a replay.
    """
    # Initialize an empty game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    
    print("Welcome to Tic Tac Toe!")
    print("Players take turns placing X and O.")
    print("To place your mark, enter the row (0-2) and column (0-2).")
    
    while not game_over:
        deftoe.print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get a valid move from the player
        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    valid_move = True
                else:
                    print("Invalid move! Please try again.")
            except ValueError:
                print("Please enter numbers between 0 and 2.")
        
        # Perform the move
        board[row][col] = current_player
        
        # Check for a win
        if deftoe.check_win(board, current_player):
            deftoe.print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        # Check for a draw
        elif deftoe.is_board_full(board):
            deftoe.print_board(board)
            print("It's a draw!")
            game_over = True
        # Switch players
        else:
            current_player = "O" if current_player == "X" else "X"
    
    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
