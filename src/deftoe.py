'''Function module for Tic Tac Toe game.This module contains functions 
    to manage the game board, check for wins, and determine if the board is full.'''  


def board_list(size, tiles):
    """Creates a list of Tic Tac Toe board of the specified size. """
    board = []
    for i in range(size):
        # Create a row with the specified size, filled with empty tiles
        board.append([tiles] * size)
    return board


def print_board(size, tiles):
    """
    Prints the board with column labels (a, b, c, ...) and row numbers (1, 2, 3, ...).

    Args:
        board (list): The 2D list representing the board.
    """

    board = board_list(size, tiles)

    # Print the column letters at the top
    column_letters = "    " + "  ".join(chr(97 + col) for col in range(size))
    print(column_letters.upper())

    # Print each row with its corresponding number label
    for i, row in enumerate(board):
        row_label = str(i + 1)  # Convert row index to a number (1, 2, 3, ...)
        row_content = " ".join(row)  # Join cells in the row with spaces
        print(row_label.rjust(2) + " " + row_content) # Add row label to the left
    print()


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
            if cell == "⬜":
                return False
    return True

def game(player1, player2):
    """
    Main function to run the Tic Tac Toe game.
    
    This function initializes the game board, manages player turns, and handles
    the game loop, including win/draw detection and prompting for a replay.
    """
    # Initialize an empty game board
    board = board_list(3, "⬜")
    current_player = player1
    game_over = False
    
    print("Welcome to Tic Tac Toe!")
    print("Players take turns placing x and O.")
    print("To place your mark, enter the row (0-2) and column (0-2).")
    
    while not game_over:
        print_board(3, "⬜")
        print(f"Player {current_player} 's turn.")
        
        # Get a valid move from the player
        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "⬜":
                    valid_move = True
                else:
                    print("Invalid move! Please try again.")
            except ValueError:
                print("Please enter numbers between 0 and 2.")
        
        # Perform the move
        board[row][col] = current_player
        
        # Check for a win
        if check_win(board, current_player):
            print_board(3, "⬜")
            print(f"Player {current_player} wins!")
            game_over = True
        # Check for a draw
        elif is_board_full(board):
            print_board(3, "⬜")
            print("It's a draw!")
            game_over = True
        # Switch players
        else:
            current_player = player2 if current_player == player1 else player1