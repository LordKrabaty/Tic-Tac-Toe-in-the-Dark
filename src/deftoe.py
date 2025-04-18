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
    print(f"Players take turns placing {player1} and {player2}.")
    print("To place your mark, enter the row (0-2) and column (0-2).")
    print(f"Player 1 is {player1} and Player 2 is {player2}.")
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
    # Check each row for a win
    for row in board:
        row_win = True  # Assume player wins in this row
        for cell in row:
            if cell != player:
                row_win = False  # If any cell is not the player's symbol, no win
                break
        if row_win:
            return True  # Return True if a winning row is found

    # Check each column for a win
    board_size = len(board)  # Get the size of the board
    for col in range(board_size):
        col_win = True  # Assume player wins in this column
        for row in range(board_size):
            if board[row][col] != player:
                col_win = False  # If any cell is not the player's symbol, no win
                break
        if col_win:
            return True  # Return True if a winning column is found

    # Check the first diagonal (top-left to bottom-right) for a win
    diagonal_win_1 = True  # Assume player wins on this diagonal
    for i in range(board_size):
        if board[i][i] != player:
            diagonal_win_1 = False  # If any cell is not the player's symbol, no win
            break
    if diagonal_win_1:
        return True  # Return True if the first diagonal is a win

    # Check the second diagonal (top-right to bottom-left) for a win
    diagonal_win_2 = True  # Assume player wins on this diagonal
    for i in range(board_size):
        if board[i][board_size - 1 - i] != player:
            diagonal_win_2 = False  # If any cell is not the player's symbol, no win
            break
    if diagonal_win_2:
        return True  # Return True if the second diagonal is a win

    # If no win condition is met, return False
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

def get_valid_move(board: List[List[str]], board_size: int, empty_tile: str) -> tuple:
    """
    Prompts the user to enter a valid move using row numbers (1, 2, 3) and column letters (A, B, C).
    
    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
        board_size (int): The size of the board (number of rows and columns).
        empty_tile (str): The symbol representing an empty tile.
    
    Returns:
        tuple: A tuple containing the valid row and column indices (0-based).
    """
    valid_move = False
    while not valid_move:
        try:
            # Prompt user for row (1-based index)
            row = int(input(f"Enter row (1-{board_size}): ")) - 1
            
            # Prompt user for column (letter A, B, C)
            col_letter = input(f"Enter column (A-{chr(65 + board_size - 1)}): ").upper()
            col = ord(col_letter) - 65
            
            # Validate move
            if 0 <= row < board_size and 0 <= col < board_size and board[row][col] == empty_tile:
                valid_move = True
                return row, col
            else:
                print("Invalid move! Please try again.")
        except Exception:
            print("Invalid input! Please enter a valid row number and column letter.")


def clear_screen():
    """
    Clears the console screen.
    """
    import os, platform

    # Check the operating system and run the appropriate command
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

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
    from copy import deepcopy
    board_with_all_moves = create_board(board_size, empty_tile) # board for showing completed moves
    board_with_hidden_moves = deepcopy(board_with_all_moves) # board for not showing completed moves
    current_player = player1
    game_over = False

    input("Press Enter to start the game...")  # Wait for user input to start the game
    clear_screen()  # Clear the console for a fresh start
    
    while not game_over:
        clear_screen() # Clear the console for not showing the moves of the other player
        print_board(board_with_hidden_moves)  # not showing the moves of the other player
        print(f"Player {current_player}'s turn.")
        
        # Get a valid move from the player
        row, col = get_valid_move(board_with_all_moves, board_size, empty_tile)
        
        # Perform the move
        board_with_all_moves[row][col] = current_player
        
        # Check for a win
        if check_win(board_with_all_moves, current_player):
            print_board(board_with_all_moves)
            print(f"Player {current_player} wins!")
            game_over = True
        # Check for a draw
        elif is_board_full(board_with_all_moves, empty_tile):
            print_board(board_with_all_moves)
            print("It's a draw!")
            game_over = True
        # Switch players
        else:
            current_player = player1 if current_player == player2 else player2

