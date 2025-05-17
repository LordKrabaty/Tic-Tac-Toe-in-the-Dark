from typing import List

"""
Function module for Tic Tac Toe game.
This module contains functions to manage the game.
"""

def instructions(player1_symbol: str, player2_symbol: str) -> None:
    """
    Displays the game instructions to the players.
    
    Args:
        player1_symbol (str): Symbol for player 1.
        player2_symbol (str): Symbol for player 2.
    """
    print("Welcome to Tic Tac Toe!")
    print("This version of Tic Tac Toe includes a unique twist: the board is (partly) hidden during play.")
    print("Players will not see the opponent's moves until they hit a non-empty tile.")
    print("If you hit a non-empty tile, it becomes permanently blocked, and the turn switches to the other player.")
    print("After hitting a non-empty tile, all previous moves are revealed on the board.")
    print(f"Players take turns placing {player1_symbol} and {player2_symbol}.")
    print("To place your mark, enter the column letter and row number (e.g., 'B2', 'A3') within the board range.")
    print(f"Player 1 is {player1_symbol} and Player 2 is {player2_symbol}.")
    print("After three moves have been made, the previous moves will be revealed (unless a reveal has already occurred).")
    print("The first player to get three in a row wins!")
    print("If the board is full and no player has three in a row, any blocked tiles will be cleared, hidden board will be reset and the game will continue.")
    print("If the board is full without any blocked tiles and no player has three in a row, it's a draw.")
    print("Let's start the game!")

def create_board(board_size: int, empty_tile: str) -> List[List[str]]:
    """
    Creates a Tic Tac Toe board of the specified size filled with empty tiles.
    
    Args:
        board_size (int): The size of the board (number of rows and columns).
        empty_tile (str): The symbol representing an empty tile.
    
    Returns:
        list: A 2D list representing the board.
    """
    board = []
    for _ in range(board_size):
        # Add a row filled with empty tiles
        board.append([empty_tile] * board_size)
    return board

def format_board(board: List[List[str]]) -> str:
        """
        Formats the current state of the board with column labels (A, B, C) and row numbers (1, 2, 3).
        Returns the formatted board as a string.
        
        Args:
            board (list): The 2D list representing the board.
        
        Returns:
            str: A string representation of the formatted board.
        """
        size = len(board)

        # Create column labels at the top
        column_labels = "    " + "  ".join(chr(65 + col) for col in range(size))
        formatted_board = column_labels + "\n"

        # Add each row with its corresponding number label
        for i, row in enumerate(board):
            row_label = str(i + 1)  # Convert row index to a number (1, 2, 3)
            row_content = " ".join(row)  # Join cells in the row with spaces
            formatted_board += row_label + "  " + row_content + "\n"  # Add row label to the left

        return formatted_board

def check_win(board: List[List[str]], player_symbol: str) -> bool:
    """
    Checks if the specified player has won the game.
    
    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
        player_symbol (str): The player symbol to check for a win.
    
    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check each row for a win
    for row in board:
        row_win = True  # Assume player wins in this row
        for cell in row:
            if cell != player_symbol:
                row_win = False  # If any cell is not the player's symbol, no win
                break
        if row_win:
            return True  # Return True if a winning row is found

    # Check each column for a win
    board_size = len(board)  # Get the size of the board
    for col in range(board_size):
        col_win = True  # Assume player wins in this column
        for row in range(board_size):
            if board[row][col] != player_symbol:
                col_win = False  # If any cell is not the player's symbol, no win
                break
        if col_win:
            return True  # Return True if a winning column is found

    # Check the first diagonal (top-left to bottom-right) for a win
    diagonal_win_1 = True  # Assume player wins on this diagonal
    for i in range(board_size):
        if board[i][i] != player_symbol:
            diagonal_win_1 = False  # If any cell is not the player's symbol, no win
            break
    if diagonal_win_1:
        return True  # Return True if the first diagonal is a win

    # Check the second diagonal (top-right to bottom-left) for a win
    diagonal_win_2 = True  # Assume player wins on this diagonal
    for i in range(board_size):
        if board[i][board_size - 1 - i] != player_symbol:
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

def parse_move(move: str) -> tuple:
    """
    Parses the user's input move into row and column indices.

    Args:
        move (str): The user's input move (e.g., 'B2', 'A10').

    Returns:
        tuple: A tuple containing the column letter and row number as strings.
    """
    col_letter = move[0]
    row_number = move[1:]
    return col_letter, row_number

def is_move_to_empty_tile(board: list, row: int, col: int, empty_tile: str) -> bool:
    """
    Checks if the given move within the board range and if the tile is empty.

    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
        row (int): The row index of the move (0-based).
        col (int): The column index of the move (0-based).
        empty_tile (str): The symbol representing a blocked tile.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    board_size = len(board)
    if 0 <= row < board_size and 0 <= col < board_size:
        return board[row][col] == empty_tile
    return False

def get_valid_move(board: list, empty_tile: str) -> tuple:
    """
    Prompts the user to enter a valid move using a single input combining
    column letter and row number (e.g., 'B2', 'A10'), with dynamic range display.

    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
        empty_tile (str): The symbol representing a blocked tile.

    Returns:
        tuple: A tuple containing the valid row and column indices (0-based).
    """
    board_size = len(board)
    valid_move = False

    while not valid_move:
        try:
            # Calculate the range of column letters and row numbers
            col_max = chr(65 + board_size - 1)
            row_max = board_size
            
            # Prompt user for move in the format 'B2', 'A10', etc.
            move = input(f"Enter your move (between A1-{col_max}{row_max}): ").strip().upper()
            
            # Parse the move
            col_letter, row_number = parse_move(move)
            
            # Convert inputs to indices
            row = int(row_number) - 1  # Convert row to 0-based index
            col = ord(col_letter) - 65  # Convert column letter to 0-based index
            
            # Validate the move
            if is_move_to_empty_tile(board, row, col, empty_tile):
                valid_move = True
                return row, col
            else:
                print("Invalid move! Please try again.")
        except (IndexError, ValueError):
            print("Invalid input! Please enter a proper input combining column letter and row number (e.g., 'B2')")
    # This line should never be reached, but ensures a tuple is always returned
    return 0, 0

def process_validated_move(row, col, board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile):
    """
    Process an already validated move on the board. If the selected tile is not empty, block it.
    Otherwise, place the current player's symbol.

    Args:
        row (int): The row index of the move.
        col (int): The column index of the move.
        board_with_all_moves (list of list of str): The board showing all moves.
        board_with_hidden_moves (list of list of str): The board with hidden moves.
        current_player_symbol (str): The symbol of the current player.
        empty_tile (str): The symbol representing an empty tile.
        blocked_tile (str): The symbol representing a blocked tile.

    Returns:
        tuple: A tuple containing the updated boards and the increment in performed moves.
    """
    from copy import deepcopy

    if board_with_all_moves[row][col] != empty_tile:
        # Tile is not empty, block it
        non_empty_tile = board_with_all_moves[row][col]
        board_with_all_moves[row][col] = blocked_tile
        board_with_hidden_moves = deepcopy(board_with_all_moves)  # Update hidden board to reveal moves
        print(f"Hit a non-empty tile ({non_empty_tile}). It is now permanently blocked. Previous moves can be seen on board. Switching turns.")
        return board_with_all_moves, board_with_hidden_moves, 1
    else:
        # Perform the move
        board_with_all_moves[row][col] = current_player_symbol
        clear_screen()  # Clear the console for not showing the moves of the other player
        return board_with_all_moves, board_with_hidden_moves, 1

def clear_tiles(board: List[List[str]], blocked_tile: str, empty_tile: str, clear_all: bool = False):
    """
    Clear tiles on the board.
    
    If `clear_all` is True, all tiles on the board will be replaced with `empty_tile`.
    Otherwise, only tiles matching `blocked_tile` will be replaced.
    
    Args:
        board (List[List[str]]): The game board.
        blocked_tile (str): The tile to be cleared (if `clear_all` is False).
        empty_tile (str): The tile to replace cleared tiles with.
        clear_all (bool): Whether to clear all tiles or just blocked tiles.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if clear_all or board[i][j] == blocked_tile:
                # Replace the tile with the empty tile
                board[i][j] = empty_tile

def check_game_status(board_with_all_moves: List[List[str]], 
                      board_hidden_moves: List[List[str]], 
                      current_player_symbol: str, 
                      empty_tile: str, 
                      blocked_tile: str) -> str:
    """
    Checks the current status of the game to determine if a player has won, 
    the game is a draw, or it should continue.

    Args:
        board_with_all_moves (List[List[str]]): The main game board showing all moves.
        board_hidden_moves (List[List[str]]): The hidden board used for additional game logic.
        current_player_symbol (str): The symbol of the current player (e.g., 'X' or 'O').
        empty_tile (str): The symbol representing an empty tile on the board.
        blocked_tile (str): The symbol representing a blocked tile on the board.

    Returns:
        str: The status of the game:
             - If a player wins, returns the player's symbol (e.g., 'X' or 'O').
             - If the game is a draw, returns "draw".
             - If the game should continue, returns "continue".
    """
    # Check if the current player has won
    if check_win(board_with_all_moves, current_player_symbol):
        print(f"Player {current_player_symbol} wins!")
        return current_player_symbol
    
    # Check if the board is full
    if is_board_full(board_with_all_moves, empty_tile):
        # If blocked tiles exist, clear them and continue the game
        if any(blocked_tile in row for row in board_with_all_moves):
            print("Clearing blocked tiles and continuing the game.")
            clear_tiles(board_with_all_moves, blocked_tile, empty_tile)  # Unblock the tiles
            clear_tiles(board_hidden_moves, blocked_tile, empty_tile, clear_all=True)  # Hide all moves
            return "continue"
        else:
            # If no blocked tiles and the board is full, it's a draw
            print("It's a draw!")
            return "draw"
    
    # If no win or draw condition is met, the game continues
    return "continue"

def switch_player(current_player: str, first_symbol: str, second_symbol: str) -> str:
    """Switch to the other player."""
    return first_symbol if current_player == second_symbol else second_symbol

def game(first_symbol: str, second_symbol: str, board_size: int, empty_tile: str, blocked_tile: str) -> str:
    """
    Main function to run the Tic Tac Toe game.
    
    This function initializes the game board, manages player turns, and handles
    the game loop, including win/draw detection and prompting for a replay.
    
    Args:
        first_symbol (str): Symbol for a player who starts the game.
        second_symbol  (str): Symbol for a player who goes next.
        board_size (int): The size of the board (number of rows and columns).
        empty_tile (str): The symbol representing an empty tile.
        blocked_tile (str): The symbol representing a blocked tile.
    Returns:
        str: symbol of winning player or "draw"
    """
    # Initialize an empty and a hidden game boards
    from copy import deepcopy
    board_with_all_moves = create_board(board_size, empty_tile)  # Board for showing all moves
    board_with_hidden_moves = deepcopy(board_with_all_moves)  # Board for hiding completed moves
    current_player_symbol = first_symbol
    game_over = False

    input("Press Enter to start the game...")  # Wait for user input to start the game
    
    clear_screen()  # Clear the console for a fresh start
    performed_moves = 0  # Initialize move count
    
    while not game_over:
        if performed_moves == 3 and not any(blocked_tile in row for row in board_with_hidden_moves):
            board_with_hidden_moves  = deepcopy(board_with_all_moves) # Moves will be revealed after a delay to reduce the first player's advantage

        print(format_board(board_with_hidden_moves))  # Not showing the moves of the other player
        print("Already perforemed moves on board:", performed_moves)

        if performed_moves < 3 and not any(blocked_tile in row for row in board_with_hidden_moves):
            print("After three moves have been made, the previous moves will be revealed (unless a reveal has already occurred).")
        print(f"Player {current_player_symbol}'s turn.")
        
        # Get a valid move from the player
        row, col = get_valid_move(board_with_hidden_moves, empty_tile)
        
        # Process the move
        board_with_all_moves, board_with_hidden_moves, move_increment = process_validated_move(
            row, col, board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile)
        performed_moves += move_increment
        
        # Check game status
        status = check_game_status(board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile)
        if status in [first_symbol, second_symbol, "draw"]:
            print(format_board(board_with_all_moves))
            return status
    
        # Switch players
        current_player_symbol = switch_player(current_player_symbol, first_symbol, second_symbol)
    
    # In case the loop exits unexpectedly, return "draw" as a fallback¨
    print("Game ended unexpectedly. No winner. It's a draw.")
    return "draw"

