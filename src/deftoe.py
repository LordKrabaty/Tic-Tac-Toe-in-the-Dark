from typing import List

"""
Function module for Tic Tac Toe game.
This module contains functions to manage the game board, check for wins, and determine if the board is full.
"""

def instructions(player1: str, player2: str) -> None:
    """
    Displays the game instructions to the players.
    
    Args:
        player1 (str): Symbol for player 1.
        player2 (str): Symbol for player 2.
    """
    print("Welcome to Tic Tac Toe!")
    print(f"Players take turns placing {player1}  and {player2}.")
    print("To place your mark, enter the row (0-2) and column (0-2).")
    print(f"Player 1 is {player1}  and Player 2 is {player2}.")
    print("The first player to get three in a row wins!")
    print("If the board is full and no player has three in a row, it's a draw.")
    print("Let's start the game!")

def create_board(size: int, empty_tile: str) -> List[List[str]]:
    """
    Creates a Tic Tac Toe board of the specified size filled with empty tiles.
    
    Args:
        size (int): The size of the board (number of rows and columns).
        empty_tile (str): The symbol representing an empty tile.
    
    Returns:
        list: A 2D list representing the board.
    """
    board = []
    for _ in range(size):
        # Add a row filled with empty tiles
        board.append([empty_tile] * size)
    return board

def print_board(board: List[List[str]]) -> None:
    """
    Prints the current state of the board with column labels (A, B, C) and row numbers (1, 2, 3).
    
    Args:
        board (list): The 2D list representing the board.
    """
    size = len(board)

    # Print column labels at the top
    column_labels = "    " + "  ".join(chr(65 + col) for col in range(size))
    print(column_labels)

    # Print each row with its corresponding number label
    for i, row in enumerate(board):
        row_label = str(i + 1)  # Convert row index to a number (1, 2, 3)
        row_content = " ".join(row)  # Join cells in the row with spaces
        print(row_label + "  " + row_content)  # Add row label to the left
    print()

def check_win(board: List[List[str]], player: str) -> bool:
    """
    Checks if the specified player has won the game.
    
    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
        player (str): The player symbol ('X' or 'O') to check for a win.
    
    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check rows for a win
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns for a win
    for col in range(len(board)):
        if all(board[row][col] == player for row in range(len(board))):
            return True
    
    # Check diagonals for a win
    if all(board[i][i] == player for i in range(len(board))) or \
       all(board[i][len(board) - 1 - i] == player for i in range(len(board))):
        return True
    
    return False

def is_board_full(board: List[List[str]], empty_tile: str) -> bool:
    """
    Checks if the game board is completely filled.
    
    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
        empty_tile (str): The symbol representing an empty tile.
    
    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if empty_tile in row:
            return False
    return True

def game(player1: str, player2: str, board_size: int, empty_tile: str) -> None:
    """
    Main function to run the Tic Tac Toe game.
    
    This function initializes the game board, manages player turns, and handles
    the game loop, including win/draw detection and prompting for a replay.
    
    Args:
        player1 (str): Symbol for player 1.
        player2 (str): Symbol for player 2.
        board_size (int): The size of the board (number of rows and columns).
        empty_tile (str): The symbol representing an empty tile.
    """
    # Initialize an empty game board
    board = create_board(board_size, empty_tile)
    current_player = player1
    game_over = False
    
    while not game_over:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get a valid move from the player
        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                
                if 0 <= row < board_size and 0 <= col < board_size and board[row][col] == empty_tile:
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
        elif is_board_full(board, empty_tile):
            print_board(board)
            print("It's a draw!")
            game_over = True
        # Switch players
        else:
            current_player = player1 if current_player == player2 else player2
