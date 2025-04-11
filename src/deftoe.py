'''Function module for Tic Tac Toe game.This module contains functions 
    to manage the game board, check for wins, and determine if the board is full.'''  


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