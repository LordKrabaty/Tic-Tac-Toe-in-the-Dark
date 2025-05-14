"""Module for testing functions."""

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

def test_format_board():
    """
    Test the `format_board` function with empty tile ⬜, for board sizes 3x3 and 9x9.
    Includes debugging prints to display actual and expected outputs.
    """
    # Test for 3x3 board
    board_3x3 = [["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"]]
    expected_output_3x3 = (
        "    A  B  C\n"
        "1  ⬜ ⬜ ⬜\n"
        "2  ⬜ ⬜ ⬜\n"
        "3  ⬜ ⬜ ⬜\n"
    )
    actual_output_3x3 = deftoe.format_board(board_3x3)

    # Assertion for 3x3 board
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


    # Assertion for 9x9 board
    assert actual_output_9x9 == expected_output_9x9

def test_check_win():
    """
    Test the `check_win` function from the `src.deftoe` module to verify its correctness for various game scenarios.
    Covers horizontal, vertical, diagonal wins, and no-win cases.
    """
    # Horizontal win scenarios
    board_3x3_horizontal = [
        ["X", "X", "X"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]
    assert deftoe.check_win(board_3x3_horizontal, "X") is True  # Top row win

    board_3x3_horizontal = [
        ["⬜", "⬜", "⬜"],
        ["O", "O", "O"],
        ["⬜", "⬜", "⬜"]
    ]
    assert deftoe.check_win(board_3x3_horizontal, "O") is True  # Middle row win

    board_3x3_horizontal = [
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["X", "X", "X"]
    ]
    assert deftoe.check_win(board_3x3_horizontal, "X") is True  # Bottom row win

    # Vertical win scenarios
    board_3x3_vertical = [
        ["X", "⬜", "⬜"],
        ["X", "⬜", "⬜"],
        ["X", "⬜", "⬜"]
    ]
    assert deftoe.check_win(board_3x3_vertical, "X") is True  # Left column win

    board_3x3_vertical = [
        ["⬜", "O", "⬜"],
        ["⬜", "O", "⬜"],
        ["⬜", "O", "⬜"]
    ]
    assert deftoe.check_win(board_3x3_vertical, "O") is True  # Middle column win

    board_3x3_vertical = [
        ["⬜", "⬜", "X"],
        ["⬜", "⬜", "X"],
        ["⬜", "⬜", "X"]
    ]
    assert deftoe.check_win(board_3x3_vertical, "X") is True  # Right column win

    # Diagonal win scenarios
    board_3x3_diagonal = [
        ["X", "⬜", "⬜"],
        ["⬜", "X", "⬜"],
        ["⬜", "⬜", "X"]
    ]
    assert deftoe.check_win(board_3x3_diagonal, "X") is True  # Top-left to bottom-right diagonal win

    board_3x3_diagonal = [
        ["⬜", "⬜", "O"],
        ["⬜", "O", "⬜"],
        ["O", "⬜", "⬜"]
    ]
    assert deftoe.check_win(board_3x3_diagonal, "O") is True  # Top-right to bottom-left diagonal win

    # No-win scenarios
    board_3x3_no_win = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"]
    ]
    assert deftoe.check_win(board_3x3_no_win, "X") is False  # No win for X
    assert deftoe.check_win(board_3x3_no_win, "O") is False  # No win for O

    board_empty = [
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]
    assert deftoe.check_win(board_empty, "X") is False  # Empty board, no win
    assert deftoe.check_win(board_empty, "O") is False  # Empty board, no win

    # Larger board scenarios (e.g., 4x4)
    board_4x4_diagonal = [
        ["X", "⬜", "⬜", "⬜"],
        ["⬜", "X", "⬜", "⬜"],
        ["⬜", "⬜", "X", "⬜"],
        ["⬜", "⬜", "⬜", "X"]
    ]
    assert deftoe.check_win(board_4x4_diagonal, "X") is True  # Top-left to bottom-right diagonal win on a 4x4 board

    board_4x4_no_win = [
        ["X", "⬜", "⬜", "⬜"],
        ["⬜", "O", "⬜", "⬜"],
        ["⬜", "⬜", "X", "⬜"],
        ["⬜", "⬜", "⬜", "O"]
    ]
    assert deftoe.check_win(board_4x4_no_win, "X") is False  # No win for X
    assert deftoe.check_win(board_4x4_no_win, "O") is False  # No win for O

def test_is_board_full():
    """
    Test the `is_board_full` function from the `deftoe` module.
    Covers scenarios for an empty board, partially filled board, and fully filled board.
    """
    # Test an empty 3x3 board
    empty_board = [
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]
    assert deftoe.is_board_full(empty_board, "⬜") is False  # Board is completely empty

    # Test a partially filled 3x3 board
    partially_filled_board = [
        ["X", "⬜", "O"],
        ["⬜", "O", "⬜"],
        ["X", "⬜", "⬜"]
    ]
    assert deftoe.is_board_full(partially_filled_board, "⬜") is False  # Board is not fully filled

    # Test a fully filled 3x3 board
    fully_filled_board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "O", "X"]
    ]
    assert deftoe.is_board_full(fully_filled_board, "⬜") is True  # Board is completely filled

    # Test an empty 4x4 board
    empty_4x4_board = [
        ["⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜"]
    ]
    assert deftoe.is_board_full(empty_4x4_board, "⬜") is False  # Larger board is completely empty

    # Test a partially filled 4x4 board
    partially_filled_4x4_board = [
        ["X", "⬜", "O", "⬜"],
        ["⬜", "O", "⬜", "X"],
        ["X", "⬜", "⬜", "O"],
        ["⬜", "⬜", "X", "⬜"]
    ]
    assert deftoe.is_board_full(partially_filled_4x4_board, "⬜") is False  # Larger board is not fully filled

    # Test a fully filled 4x4 board
    fully_filled_4x4_board = [
        ["X", "O", "X", "O"],
        ["O", "X", "O", "X"],
        ["X", "O", "X", "O"],
        ["O", "X", "O", "X"]
    ]
    assert deftoe.is_board_full(fully_filled_4x4_board, "⬜") is True  # Larger board is completely filled

def test_clear_screen():
    """
    Test the `clear_screen` function from the `deftoe` module.
    Ensures the correct system command is executed based on the operating system.
    """
    import os
    import platform
    from unittest.mock import patch

    # Mock the os.system call to verify the correct command is used
    with patch("os.system") as mock_system:
        # Test for Windows
        with patch("platform.system", return_value="Windows"):
            deftoe.clear_screen()
            mock_system.assert_called_once_with('cls')  # Ensure 'cls' is called on Windows

        # Reset the mock for the next test
        mock_system.reset_mock()

        # Test for non-Windows (e.g., Linux/Mac)
        with patch("platform.system", return_value="Linux"):
            deftoe.clear_screen()
            mock_system.assert_called_once_with('clear')  # Ensure 'clear' is called on Linux/Mac

def test_parse_move():
    """
    Test the `deftoe.parse_move` function.
    Focuses on valid inputs and edge cases, ensuring correct parsing of input.
    """
    # Valid inputs
    assert deftoe.parse_move("A1") == ("A", "1")  # Single-digit row
    assert deftoe.parse_move("B10") == ("B", "10")  # Double-digit row
    assert deftoe.parse_move("Z99") == ("Z", "99")  # Large column and row

    # Edge cases
    assert deftoe.parse_move("X0") == ("X", "0")  # Row number 0
    assert deftoe.parse_move("A01") == ("A", "01")  # Leading zero in row number

def test_is_move_to_empty_tile():
    """
    Ensures correct validation of moves on a Tic Tac Toe board.
    Covers basic functionality, edge cases, and invalid moves.
    """
    empty_tile = "⬜"  # Define the symbol for an empty tile

    # Scenario 1: Basic functionality
    board = [
        ["⬜", "X", "O"],
        ["O", "⬜", "X"],
        ["X", "O", "⬜"]
    ]
    assert deftoe.is_move_to_empty_tile(board, 0, 0, empty_tile) is True  # Empty tile at (0, 0)
    assert deftoe.is_move_to_empty_tile(board, 1, 1, empty_tile) is True  # Empty tile at (1, 1)
    assert deftoe.is_move_to_empty_tile(board, 2, 2, empty_tile) is True  # Empty tile at (2, 2)
    assert deftoe.is_move_to_empty_tile(board, 0, 1, empty_tile) is False  # Occupied by "X"
    assert deftoe.is_move_to_empty_tile(board, 1, 2, empty_tile) is False  # Occupied by "X"

    # Scenario 2: Edge cases (out of bounds)
    assert deftoe.is_move_to_empty_tile(board, -1, 0, empty_tile) is False  # Row index out of bounds
    assert deftoe.is_move_to_empty_tile(board, 0, -1, empty_tile) is False  # Column index out of bounds
    assert deftoe.is_move_to_empty_tile(board, 3, 0, empty_tile) is False  # Row index out of bounds
    assert deftoe.is_move_to_empty_tile(board, 0, 3, empty_tile) is False  # Column index out of bounds
    assert deftoe.is_move_to_empty_tile(board, 3, 3, empty_tile) is False  # Both indices out of bounds

    # Scenario 3: Empty board
    empty_board = []  # Completely empty board
    assert deftoe.is_move_to_empty_tile(empty_board, 0, 0, empty_tile) is False  # Empty board

    # Scenario 4: Larger board
    large_board = [
        ["⬜"] * 10 for _ in range(10)
    ]
    assert deftoe.is_move_to_empty_tile(large_board, 5, 5, empty_tile) is True  # Valid move in the middle
    assert deftoe.is_move_to_empty_tile(large_board, 9, 9, empty_tile) is True  # Valid move in the bottom-right corner
    assert deftoe.is_move_to_empty_tile(large_board, 10, 10, empty_tile) is False  # Out of bounds

    # Scenario 5: Different empty tile representation
    custom_empty_tile = "-"
    custom_board = [
        ["-", "X", "O"],
        ["O", "-", "X"],
        ["X", "O", "-"]
    ]
    assert deftoe.is_move_to_empty_tile(custom_board, 0, 0, custom_empty_tile) is True  # Empty tile at (0, 0)
    assert deftoe.is_move_to_empty_tile(custom_board, 1, 2, custom_empty_tile) is False  # Occupied by "X"

def test_valid_move_input():
    """
    Test the input and validation loop for user moves.
    Ensures that valid moves are accepted and invalid inputs are handled correctly.
    Covers scenarios such as valid moves, invalid formats, out-of-range moves, and occupied tiles.
    """
    from unittest.mock import patch
    empty_tile = "⬜"
    board = [
        ["⬜", "X", "O"],
        ["O", "⬜", "X"],
        ["X", "O", "⬜"]
    ]

    # Scenario 1: Valid move (e.g., 'A1')
    with patch('builtins.input', side_effect=["A1"]):  # Simulate valid user input
        row, col = deftoe.get_valid_move(board, empty_tile)
        assert (row, col) == (0, 0)  # A1 corresponds to (0, 0)

    # Scenario 2: Invalid input format followed by valid input
    with patch('builtins.input', side_effect=["AA", "B2"]):  # Invalid input followed by valid input
        row, col = deftoe.get_valid_move(board, empty_tile)
        assert (row, col) == (1, 1)  # B2 corresponds to (1, 1)

    # Scenario 3: Out-of-range move followed by valid input
    with patch('builtins.input', side_effect=["D4", "C3"]):  # Out-of-range input followed by valid input
        row, col = deftoe.get_valid_move(board, empty_tile)
        assert (row, col) == (2, 2)  # C3 corresponds to (2, 2)

    # Scenario 4: Occupied tile followed by valid input
    with patch('builtins.input', side_effect=["B1", "C3"]):  # Occupied tile followed by valid input
        row, col = deftoe.get_valid_move(board, empty_tile)
        assert (row, col) == (2, 2)  # C3 corresponds to (2, 2)

    # Scenario 5: Multiple invalid inputs before a valid move
    with patch('builtins.input', side_effect=(["", "123", "A0", "C3"])):  # Multiple invalid inputs followed by valid input
        row, col = deftoe.get_valid_move(board, empty_tile)
        assert (row, col) == (2, 2)  # C3 corresponds to (2, 2)

def test_clear_blocked_tiles():
    """
    Test the `clear_blocked_tiles` function to ensure it correctly replaces
    all occurrences of the blocked tile with the empty tile on the board.
    Scenarios include a board with no blocked tiles, a board with some blocked tiles,
    and a board with all blocked tiles.
    """
    blocked_tile = "⬛"
    empty_tile = "⬜"

    # Scenario 1: Board with no blocked tiles
    board_no_blocked = [
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]
    expected_no_blocked = [
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]
    deftoe.clear_blocked_tiles(board_no_blocked, blocked_tile, empty_tile)
    assert board_no_blocked == expected_no_blocked  # No change expected

    # Scenario 2: Board with some blocked tiles
    board_some_blocked = [
        ["⬜", "⬛", "⬜"],
        ["⬛", "⬜", "⬜"],
        ["⬜", "⬜", "⬛"]
    ]
    expected_some_blocked = [
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]
    deftoe.clear_blocked_tiles(board_some_blocked, blocked_tile, empty_tile)
    assert board_some_blocked == expected_some_blocked  # Blocked tiles replaced

    # Scenario 3: Board with all blocked tiles
    board_all_blocked = [
        ["⬛", "⬛", "⬛"],
        ["⬛", "⬛", "⬛"],
        ["⬛", "⬛", "⬛"]
    ]
    expected_all_blocked = [
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]
    deftoe.clear_blocked_tiles(board_all_blocked, blocked_tile, empty_tile)
    assert board_all_blocked == expected_all_blocked  # All tiles replaced

def test_check_game_status():
    """
    Test the `check_game_status` function to ensure it correctly identifies
    the game status as a win, draw, or continuation.
    Scenarios include a winning board, a full board resulting in a draw,
    a full board with blocked tiles, and a board that should continue.
    """
    # Mock dependencies
    def mock_check_win(board, symbol):
        return any(all(cell == symbol for cell in row) for row in board)

    def mock_is_board_full(board, empty_tile):
        return all(cell != empty_tile for row in board for cell in row)

    # Patch the dependencies
    global check_win, is_board_full
    check_win = mock_check_win
    is_board_full = mock_is_board_full

    current_player_symbol = "X"
    empty_tile = "⬜"
    blocked_tile = "⬛"

    # Scenario 1: Winning board
    winning_board = [
        ["X", "X", "X"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]
    assert deftoe.check_game_status(winning_board, current_player_symbol, empty_tile, blocked_tile) == "X"  # Player X wins

    # Scenario 2: Full board with draw
    full_draw_board = [
        ["X", "O", "X"],
        ["X", "X", "O"],
        ["O", "X", "O"]
    ]
    assert deftoe.check_game_status(full_draw_board, current_player_symbol, empty_tile, blocked_tile) == "draw"  # It's a draw

    # Scenario 3: Full board with blocked tiles
    full_blocked_board = [
        ["X", "O", "X"],
        ["⬛", "X", "O"],
        ["O", "X", "⬛"]
    ]
    assert deftoe.check_game_status(full_blocked_board, current_player_symbol, empty_tile, blocked_tile) == "continue"  # Clear blocked tiles and continue

    # Scenario 4: Board that should continue
    ongoing_board = [
        ["X", "O", "⬜"],
        ["X", "⬜", "O"],
        ["O", "X", "⬜"]
    ]
    assert deftoe.check_game_status(ongoing_board, current_player_symbol, empty_tile, blocked_tile) == "continue"  # Game should continue







