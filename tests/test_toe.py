"""Module for testing functions."""

from src import deftoe
import pytest


from src import deftoe

def test_create_board():
    """
    Test the `create_board` function with various scenarios, including standard board sizes,
    edge cases, and custom empty tile symbols.
    """
    # Standard board sizes
    assert deftoe.create_board(3, "-") == [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]  # 3x3 board
    assert deftoe.create_board(5, " ") == [[" ", " ", " ", " ", " "], 
                                           [" ", " ", " ", " ", " "], 
                                           [" ", " ", " ", " ", " "], 
                                           [" ", " ", " ", " ", " "], 
                                           [" ", " ", " ", " ", " "]]  # 5x5 board

    # Edge case: Minimum board size
    assert deftoe.create_board(1, "X") == [["X"]]  # 1x1 board

    # Edge case: Large board size
    large_board = deftoe.create_board(10, "O")
    assert len(large_board) == 10  # 10 rows
    assert all(len(row) == 10 for row in large_board)  # Each row has 10 columns
    assert all(cell == "O" for row in large_board for cell in row)  # All cells are "O"

    # Custom empty tile symbols
    assert deftoe.create_board(3, "*") == [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]  # Using '*' as empty tile
    assert deftoe.create_board(2, "") == [["", ""], ["", ""]]  # Using empty string as empty tile

from src import deftoe

def test_format_board():
    """
    Test the `format_board` function with various scenarios, including standard board sizes,
    edge cases, and custom symbols.
    """
    # Standard 3x3 board
    board_3x3 = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    expected_output_3x3 = (
        "    A  B  C\n"
        "1  - - -\n"
        "2  - - -\n"
        "3  - - -\n"
    )
    assert deftoe.format_board(board_3x3) == expected_output_3x3  # 3x3 board with '-' as empty tiles







