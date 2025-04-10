def print_board(board):
    """
    Prints the game board in a formatted style.
    
    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
    """
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n-------------")


def check_win(board, player):
    """
    Checks if the specified player has won the game.
    
    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
        player (str): The player symbol ('X' or 'O') to check for a win.
    
    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check rows for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    
    # Check columns for a win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    
    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False


def is_board_full(board):
    """
    Checks if the game board is completely filled.
    
    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
    
    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


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
        print_board(board)
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
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        # Check for a draw
        elif is_board_full(board):
            print_board(board)
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
