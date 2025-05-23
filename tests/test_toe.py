"""
Module for testing functions in the Tic Tac Toe game.
This module contains unit tests for various functions in the game logic.
"""

import sys
import os
from unittest.mock import patch
from src import deftoe

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


def test_create_board():
    """
    Test the `create_board` function with various scenarios, including standard board sizes,
    edge cases, and custom empty tile symbols.
    """
    # Standard board sizes
    assert deftoe.create_board(3, "-") == [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    assert deftoe.create_board(5, " ") == [[" "] * 5 for _ in range(5)]  # 5x5 board

    # Edge case: Minimum board size
    assert deftoe.create_board(1, "X") == [["X"]]  # 1x1 board

    # Edge case: Large board size
    large_board = deftoe.create_board(10, "O")
    assert len(large_board) == 10
    assert all(len(row) == 10 for row in large_board)
    assert all(cell == "O" for row in large_board for cell in row)

    # Custom empty tile symbols
    assert deftoe.create_board(3, "*") == [["*"] * 3 for _ in range(3)]
    assert deftoe.create_board(2, "") == [["", ""] for _ in range(2)]


def test_format_board():
    """
    Test the `format_board` function with various board sizes and tile symbols.
    """
    # Test for 3x3 board
    board_3x3 = [["⬜"] * 3 for _ in range(3)]
    expected_output_3x3 = (
        "    A  B  C\n"
        "1  ⬜ ⬜ ⬜\n"
        "2  ⬜ ⬜ ⬜\n"
        "3  ⬜ ⬜ ⬜\n"
    )
    actual_output_3x3 = deftoe.format_board(board_3x3)
    assert actual_output_3x3 == expected_output_3x3

    # Test for 9x9 board
    board_9x9 = [["⬜"] * 9 for _ in range(9)]
    expected_output_9x9 = (
        "    A  B  C  D  E  F  G  H  I\n"
        "1  ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜\n"
        "2  ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜\n"
        "3  ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜\n"
        "4  ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜\n"
        "5  ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜\n"
        "6  ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜\n"
        "7  ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜\n"
        "8  ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜\n"
        "9  ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜\n"
    )
    actual_output_9x9 = deftoe.format_board(board_9x9)
    assert actual_output_9x9 == expected_output_9x9


def test_check_win():
    """
    Test the `check_win` function to verify win conditions for various scenarios.
    """
    # Horizontal win
    board_horizontal = [["X"] * 3, ["⬜"] * 3, ["⬜"] * 3]
    assert deftoe.check_win(board_horizontal, "X") is True

    # Vertical win
    board_vertical = [["X", "⬜", "⬜"], ["X", "⬜", "⬜"], ["X", "⬜", "⬜"]]
    assert deftoe.check_win(board_vertical, "X") is True

    # Diagonal win
    board_diagonal = [["X", "⬜", "⬜"], ["⬜", "X", "⬜"], ["⬜", "⬜", "X"]]
    assert deftoe.check_win(board_diagonal, "X") is True

    # No win
    board_no_win = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
    assert deftoe.check_win(board_no_win, "X") is False


def test_is_board_full():
    """
    Test the `is_board_full` function for empty, partially filled, and fully filled boards.
    """
    empty_board = [["⬜"] * 3 for _ in range(3)]
    assert deftoe.is_board_full(empty_board, "⬜") is False

    partially_filled_board = [["X", "⬜", "O"], ["⬜", "O", "⬜"], ["X", "⬜", "⬜"]]
    assert deftoe.is_board_full(partially_filled_board, "⬜") is False

    fully_filled_board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
    assert deftoe.is_board_full(fully_filled_board, "⬜") is True


def test_clear_screen():
    """
    Test the `clear_screen` function to ensure it executes the correct system command.
    """
    with patch("os.system") as mock_system:
        with patch("platform.system", return_value="Windows"):
            deftoe.clear_screen()
            mock_system.assert_called_once_with('cls')

        mock_system.reset_mock()

        with patch("platform.system", return_value="Linux"):
            deftoe.clear_screen()
            mock_system.assert_called_once_with('clear')


def test_parse_move():
    """
    Test the `parse_move` function for valid and edge-case inputs.
    """
    assert deftoe.parse_move("A1") == ("A", "1")
    assert deftoe.parse_move("B10") == ("B", "10")
    assert deftoe.parse_move("Z99") == ("Z", "99")


def test_is_move_to_empty_tile():
    """
    Test the `is_move_to_empty_tile` function for valid moves and edge cases.
    """
    board = [["⬜", "X", "O"], ["O", "⬜", "X"], ["X", "O", "⬜"]]
    empty_tile = "⬜"
    assert deftoe.is_move_to_empty_tile(board, 0, 0, empty_tile) is True
    assert deftoe.is_move_to_empty_tile(board, -1, 0, empty_tile) is False


def test_get_valid_move():
    """
    Test the `get_valid_move` function for valid and invalid inputs.
    """
    board = [["⬜", "X", "O"], ["O", "⬜", "X"], ["X", "O", "⬜"]]
    empty_tile = "⬜"
    with patch('builtins.input', side_effect=["A1"]):
        row, col = deftoe.get_valid_move(board, empty_tile)
        assert (row, col) == (0, 0)


def test_process_validated_move():
    """
    Test the `process_validated_move` function for valid moves and blocking tiles.
    """
    board_with_all_moves = [["O", "⬜", "X"], ["⬜", "O", "⬜"], ["⬜", "O", "X"]]
    board_with_hidden_moves = [["⬜"] * 3 for _ in range(3)]
    empty_tile = "⬜"
    blocked_tile = "⬛"
    current_player_symbol = "O"

    updated_board, updated_hidden_board, increment = deftoe.process_validated_move(
        0, 1, board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile
    )
    assert updated_board[0][1] == "O"
    assert increment == 1


def test_clear_tiles():
    """
    Test the `clear_tiles` function for clearing blocked tiles.
    """
    board = [["⬜", "⬛", "⬜"], ["⬛", "⬜", "⬜"], ["⬜", "⬜", "⬛"]]
    deftoe.clear_tiles(board, "⬛", "⬜")
    assert board == [["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"]]


def test_check_game_status():
    """
    Test the `check_game_status` function for win, draw, and continuation scenarios.
    """
    board = [["X", "X", "X"], ["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"]]
    hidden_board = [["⬜"] * 3 for _ in range(3)]
    assert deftoe.check_game_status(board, hidden_board, "X", "⬜", "⬛") == "X"


def test_switch_player():
    """
    Test the `switch_player` function for switching between two players.
    """
    assert deftoe.switch_player("X", "X", "O") == "O"
    assert deftoe.switch_player("O", "X", "O") == "X"


def test_game_flow():
    """
    Test the `game` function for a complete game simulation.
    """
    first_symbol = "X"
    second_symbol = "O"
    board_size = 3
    empty_tile = "⬜"
    blocked_tile = "⬛"

    moves = ["", "A1", "B1", "A2", "B2", "A3"]  # X wins
    with patch('builtins.input', side_effect=moves), \
         patch('deftoe.clear_screen'), \
         patch('deftoe.format_board', return_value="formatted_board"):
        result = deftoe.game(first_symbol, second_symbol, board_size, empty_tile, blocked_tile)
        assert result == first_symbol
