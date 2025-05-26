from typing import List
from copy import deepcopy
import os
import platform
import random

"""
Function module for Tic Tac Toe game.
This module contains functions to manage the game.
"""

def clear_screen() -> None:
    """
    Clears the console screen.
    """
    # Check the operating system and run the appropriate command
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


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
    return [[empty_tile] * board_size for _ in range(board_size)]


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
    column_labels = "    " + "  ".join(chr(65 + col) for col in range(size))
    formatted_board = column_labels + "\n"

    for i, row in enumerate(board):
        row_label = str(i + 1)
        row_content = " ".join(row)
        formatted_board += row_label + "  " + row_content + "\n"

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
    size = len(board)
    for row in board:
        if all(cell == player_symbol for cell in row):
            return True

    for col in range(size):
        if all(board[row][col] == player_symbol for row in range(size)):
            return True

    if all(board[i][i] == player_symbol for i in range(size)):
        return True

    if all(board[i][size - 1 - i] == player_symbol for i in range(size)):
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
    return all(empty_tile not in row for row in board)


def parse_move(move: str) -> tuple:
    """
    Parses the user's input move into row and column indices.

    Args:
        move (str): The user's input move (e.g., 'B2', 'A10').

    Returns:
        tuple: A tuple containing the column letter and row number as strings.
    """
    return move[0], move[1:]


def is_move_to_empty_tile(board: List[List[str]], row: int, col: int, empty_tile: str) -> bool:
    """
    Checks if the given move is within the board range and if the tile is empty.

    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
        row (int): The row index of the move (0-based).
        col (int): The column index of the move (0-based).
        empty_tile (str): The symbol representing an empty tile.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    return 0 <= row < len(board) and 0 <= col < len(board) and board[row][col] == empty_tile


def get_valid_move(board: List[List[str]], empty_tile: str) -> tuple:
    """
    Prompts the user to enter a valid move using a single input combining
    column letter and row number (e.g., 'B2', 'A10'), with dynamic range display.

    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
        empty_tile (str): The symbol representing an empty tile.

    Returns:
        tuple: A tuple containing the valid row and column indices (0-based).
    """
    board_size = len(board)

    while True:
        try:
            col_max = chr(65 + board_size - 1)
            row_max = board_size
            move = input(f"Enter your move (between A1-{col_max}{row_max}): ").strip().upper()
            col_letter, row_number = parse_move(move)
            row = int(row_number) - 1
            col = ord(col_letter) - 65

            if is_move_to_empty_tile(board, row, col, empty_tile):
                return row, col

            print("Invalid move! Please try again.")
        except (IndexError, ValueError):
            print("Invalid input! Please enter a proper input combining column letter and row number (e.g., 'B2').")


def clear_tiles(board: List[List[str]], blocked_tile: str, empty_tile: str, clear_all: bool = False) -> None:
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
                board[i][j] = empty_tile


def process_validated_move(row: int, col: int, board_with_all_moves: List[List[str]], 
                           board_with_hidden_moves: List[List[str]], current_player_symbol: str, 
                           empty_tile: str, blocked_tile: str) -> tuple:
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
    if board_with_all_moves[row][col] != empty_tile:
        board_with_all_moves[row][col] = blocked_tile
        board_with_hidden_moves = deepcopy(board_with_all_moves)
        print(f"Hit a non-empty tile. It is now permanently blocked. Previous moves can be seen on board.")
        return board_with_all_moves, board_with_hidden_moves, 1
    else:
        board_with_all_moves[row][col] = current_player_symbol
        clear_screen()
        return board_with_all_moves, board_with_hidden_moves, 1


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
    if check_win(board_with_all_moves, current_player_symbol):
        print(f"Player {current_player_symbol} wins!")
        return current_player_symbol

    if is_board_full(board_with_all_moves, empty_tile):
        if any(blocked_tile in row for row in board_with_all_moves):
            print("Clearing blocked tiles and continuing the game.")
            clear_tiles(board_with_all_moves, blocked_tile, empty_tile)
            clear_tiles(board_hidden_moves, blocked_tile, empty_tile, clear_all=True)
            return "continue"
        else:
            print("It's a draw!")
            return "draw"

    return "continue"


def switch_player(current_player: str, first_symbol: str, second_symbol: str) -> str:
    """
    Switches to the other player.
    
    Args:
        current_player (str): The symbol of the current player.
        first_symbol (str): The symbol of the first player.
        second_symbol (str): The symbol of the second player.

    Returns:
        str: The symbol of the next player.
    """
    return first_symbol if current_player == second_symbol else second_symbol


def game(first_symbol: str, second_symbol: str, board_size: int, empty_tile: str, blocked_tile: str) -> str:
    """
    Main function to run the Tic Tac Toe game.
    
    This function initializes the game board, manages player turns, and handles
    the game loop, including win/draw detection and prompting for a replay.
    
    Args:
        first_symbol (str): Symbol for a player who starts the game.
        second_symbol (str): Symbol for a player who goes next.
        board_size (int): The size of the board (number of rows and columns).
        empty_tile (str): The symbol representing an empty tile.
        blocked_tile (str): The symbol representing a blocked tile.
    
    Returns:
        str: Symbol of the winning player or "draw".
    """
    board_with_all_moves = create_board(board_size, empty_tile)
    board_with_hidden_moves = deepcopy(board_with_all_moves)
    current_player_symbol = first_symbol
    game_over = False
    performed_moves = 0

    input("Press Enter to start the game...")
    clear_screen()

    while not game_over:
        if performed_moves == 3 and not any(blocked_tile in row for row in board_with_hidden_moves):
            board_with_hidden_moves = deepcopy(board_with_all_moves)

        print(format_board(board_with_hidden_moves))
        print(f"Performed moves: {performed_moves}")
        if performed_moves < 3:
            print("After three moves have been made, the previous moves will be revealed.")

        print(f"Player {current_player_symbol}'s turn.")
        row, col = get_valid_move(board_with_hidden_moves, empty_tile)
        board_with_all_moves, board_with_hidden_moves, move_increment = process_validated_move(
            row, col, board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile
        )
        performed_moves += move_increment

        status = check_game_status(board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile)
        if status in [first_symbol, second_symbol, "draw"]:
            print(format_board(board_with_all_moves))
            return status

        current_player_symbol = switch_player(current_player_symbol, first_symbol, second_symbol)

    print("Game ended unexpectedly. No winner. It's a draw.")
    return "draw"


def game_vs_random_computer(player_symbol: str, computer_symbol: str, board_size: int, empty_tile: str, blocked_tile: str) -> str:
    """
    Variant of the game where the player plays against a random-move computer.

    Args:
        player_symbol (str): Symbol for the human player.
        computer_symbol (str): Symbol for the computer.
        board_size (int): The size of the board (number of rows and columns).
        empty_tile (str): The symbol representing an empty tile.
        blocked_tile (str): The symbol representing a blocked tile.

    Returns:
        str: Symbol of the winning player or "draw".
    """
    board_with_all_moves = create_board(board_size, empty_tile)
    board_with_hidden_moves = deepcopy(board_with_all_moves)
    current_player_symbol = player_symbol
    game_over = False
    performed_moves = 0

    input("Press Enter to start the game against the computer...")
    clear_screen()

    while not game_over:
        if performed_moves == 3 and not any(blocked_tile in row for row in board_with_hidden_moves):
            board_with_hidden_moves = deepcopy(board_with_all_moves)

        print(format_board(board_with_hidden_moves))
        print(f"Performed moves: {performed_moves}")
        if performed_moves < 3:
            print("After three moves have been made, the previous moves will be revealed.")

        print(f"Player {current_player_symbol}'s turn.")

        if current_player_symbol == player_symbol:
            row, col = get_valid_move(board_with_hidden_moves, empty_tile)
        else:
            # Computer move: pick a random empty tile
            empty_positions = [
                (i, j)
                for i in range(board_size)
                for j in range(board_size)
                if board_with_hidden_moves[i][j] == empty_tile
            ]
            row, col = random.choice(empty_positions)

        board_with_all_moves, board_with_hidden_moves, move_increment = process_validated_move(
            row, col, board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile
        )
        performed_moves += move_increment

        status = check_game_status(board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile)
        if status in [player_symbol, computer_symbol, "draw"]:
            print(format_board(board_with_all_moves))
            return status

        current_player_symbol = switch_player(current_player_symbol, player_symbol, computer_symbol)

    print("Game ended unexpectedly. No winner. It's a draw.")
    return "draw"


def game_vs_smart_computer(player_symbol: str, computer_symbol: str, board_size: int, empty_tile: str, blocked_tile: str) -> str:
    """
    Variant of the game where the player plays against a smarter computer.
    The computer will try to win if possible, block the player if needed, otherwise pick randomly.

    Args:
        player_symbol (str): Symbol for the human player.
        computer_symbol (str): Symbol for the computer.
        board_size (int): The size of the board (number of rows and columns).
        empty_tile (str): The symbol representing an empty tile.
        blocked_tile (str): The symbol representing a blocked tile.

    Returns:
        str: Symbol of the winning player or "draw".
    """
    def find_winning_move(board, symbol):
        # Try all empty positions, return the first that leads to a win
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == empty_tile:
                    board[i][j] = symbol
                    if check_win(board, symbol):
                        board[i][j] = empty_tile
                        return (i, j)
                    board[i][j] = empty_tile
        return None

    board_with_all_moves = create_board(board_size, empty_tile)
    board_with_hidden_moves = deepcopy(board_with_all_moves)
    current_player_symbol = player_symbol
    game_over = False
    performed_moves = 0

    input("Press Enter to start the game against the smart computer...")
    clear_screen()

    while not game_over:
        if performed_moves == 3 and not any(blocked_tile in row for row in board_with_hidden_moves):
            board_with_hidden_moves = deepcopy(board_with_all_moves)

        print(format_board(board_with_hidden_moves))
        print(f"Performed moves: {performed_moves}")
        if performed_moves < 3:
            print("After three moves have been made, the previous moves will be revealed.")

        print(f"Player {current_player_symbol}'s turn.")

        if current_player_symbol == player_symbol:
            row, col = get_valid_move(board_with_hidden_moves, empty_tile)
        else:
            # Smart computer logic
            # 1. Win if possible
            move = find_winning_move(board_with_all_moves, computer_symbol)
            # 2. Block player if possible
            if move is None:
                move = find_winning_move(board_with_all_moves, player_symbol)
            # 3. Otherwise, pick random
            if move is None:
                empty_positions = [
                    (i, j)
                    for i in range(board_size)
                    for j in range(board_size)
                    if board_with_hidden_moves[i][j] == empty_tile
                ]
                move = random.choice(empty_positions)
            row, col = move
            print(f"Computer chooses: {chr(65 + col)}{row + 1}")

        board_with_all_moves, board_with_hidden_moves, move_increment = process_validated_move(
            row, col, board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile
        )
        performed_moves += move_increment

        status = check_game_status(board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile)
        if status in [player_symbol, computer_symbol, "draw"]:
            print(format_board(board_with_all_moves))
            return status

        current_player_symbol = switch_player(current_player_symbol, player_symbol, computer_symbol)

    print("Game ended unexpectedly. No winner. It's a draw.")
    return "draw"
