"""Module for testing functions."""

from src import deftoe
import sys
import os
from unittest.mock import patch

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


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

def test_process_validated_move():
    """
    Test the `process_validated_move` function to ensure it correctly handles moves and blocking on the board.
    """

    # Initial setup for the tests
    empty_tile = "⬜"
    blocked_tile = "⬛"
    current_player_symbol = "O"
    board_with_all_moves = [
        ["O", "⬜", "X"],
        ["⬜", "O", "⬜"],
        ["⬜", "O", "X"]
    ]
    board_with_hidden_moves = [
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]

    # Scenario 1: Place a move on an empty tile
    updated_board, updated_hidden_board, increment = deftoe.process_validated_move(0, 1, board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile)
    assert updated_board[0][1] == "O"  # The move should place 'O' on the board
    assert updated_hidden_board == board_with_hidden_moves  # Hidden board should remain unchanged
    assert increment == 1  # Move should increment the move count by 1

    # Scenario 2: Block a non-empty tile
    updated_board, updated_hidden_board, increment = deftoe.process_validated_move(0, 0, board_with_all_moves, board_with_hidden_moves, current_player_symbol, empty_tile, blocked_tile)
    assert updated_board[0][0] == "⬛"  # The non-empty tile should be blocked
    assert updated_hidden_board[0][0] == "⬛"  # Hidden board should reveal the blocked tile
    assert increment == 1  # Blocking should also increment the move count by 1

def test_clear_tiles():
    """
    Test the `clear_tiles` function to ensure it correctly replaces
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
    deftoe.clear_tiles(board_no_blocked, blocked_tile, empty_tile)
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
    deftoe.clear_tiles(board_some_blocked, blocked_tile, empty_tile)
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
    deftoe.clear_tiles(board_all_blocked, blocked_tile, empty_tile)
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

    board_hidden_moves = [
        ["X", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["O", "X", "⬜"]
    ]


    # Scenario 1: Winning board
    winning_board = [
        ["X", "X", "X"],
        ["⬜", "⬜", "⬜"],
        ["O", "X", "⬜"]
    ]
    assert deftoe.check_game_status(winning_board, board_hidden_moves, current_player_symbol, empty_tile, blocked_tile) == "X"  # Player X wins

    # Scenario 2: Full board with draw
    full_draw_board = [
        ["X", "O", "X"],
        ["X", "X", "O"],
        ["O", "X", "O"]
    ]
    assert deftoe.check_game_status(full_draw_board, board_hidden_moves, current_player_symbol, empty_tile, blocked_tile) == "draw"  # It's a draw

    # Scenario 3: Full board with blocked tiles
    full_blocked_board = [
        ["X", "O", "X"],
        ["⬛", "X", "O"],
        ["O", "X", "⬛"]
    ]

    ublocked_board = [
        ["X", "O", "X"],
        ["⬜", "X", "O"],
        ["O", "X", "⬜"]
    ]

    reset_board = [
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜"]
    ]

    assert deftoe.check_game_status(full_blocked_board, board_hidden_moves, current_player_symbol, empty_tile, blocked_tile) == "continue"  # Clear blocked tiles and continue
    assert full_blocked_board == ublocked_board
    assert board_hidden_moves == reset_board

    # Scenario 4: Board that should continue
    ongoing_board = [
        ["X", "O", "⬜"],
        ["X", "⬜", "O"],
        ["O", "X", "⬜"]
    ]
    assert deftoe.check_game_status(ongoing_board, board_hidden_moves, current_player_symbol, empty_tile, blocked_tile) == "continue"  # Game should continue

def test_switch_player():
    """
    Test the `switch_player` function to ensure it correctly switches between two players.
    """

    # Scenario 1: Switch from first player to second player
    assert deftoe.switch_player("X", "X", "O") == "O"  # Current player is "X", should switch to "O"
    assert deftoe.switch_player("O", "O", "X") == "X"  # Current player is "O", should switch to "X"

    # Scenario 2: Switch from second player to first player
    assert deftoe.switch_player("O", "X", "O") == "X"  # Current player is "O", should switch to "X"
    assert deftoe.switch_player("X", "O", "X") == "O"  # Current player is "X", should switch to "O"

    # Scenario 3: Ensure consistency with repeated switches
    current_player = "X"
    for _ in range(10):
        current_player = deftoe.switch_player(current_player, "X", "O")
    assert current_player == "X"  # After 10 switches, should return to original player "X"

def test_game_invalidMove_firstPlayerWin():
    """
    Test the `game` function for a scenario where the first player wins.

    The test simulates a full game where both players make valid moves, and the first
    player achieves a winning line without hitting non-empty tiles, making wrong moves,
    or requiring the board to be full.
    """
    first_symbol = "X"
    second_symbol = "O"
    board_size = 3
    empty_tile = "⬜"
    blocked_tile = "⬛"

    # Define a sequence of moves in the user input format (e.g., 'A1', 'B2')
    # These moves lead to a win for the first player with one invalid move.
    moves = [
        "",     # Simulate hitting Enter at the start
        "A1",   # 1. X
        "B1",   # 2. O
        "1A",   # invalid move
        "A2",   # 3. X
        "B2",   # 4. O
        "A3"    # 5. X (winning move - vertical line in column A)
    ]

    # Mock the input function to return moves in sequence
    with patch('builtins.input', side_effect=moves), \
         patch('deftoe.clear_screen'), \
         patch('deftoe.format_board', return_value="formatted_board"):

        # Run the game function
        result = deftoe.game(first_symbol, second_symbol, board_size, empty_tile, blocked_tile)

        # Assert that the game ends with the first player winning
        assert result == first_symbol, "The game should have ended with the first player winning."

def test_game_invalidMoves_draw():
    """
    Test the `game` function for a wrong move and a scenario where the game ends in a draw.
    """
    first_symbol = "X"
    second_symbol = "O"
    board_size = 3
    empty_tile = "⬜"
    blocked_tile = "⬛"

    # Define a sequence of moves in the user input format (e.g., 'A1', 'B2')
    # These moves lead to a draw. The first input simulates hitting Enter. There are also 3 invalid moves during game.
    moves = [
        "",     # Simulate hitting Enter at the start
        "y",   # inalid move
        "",    # inalid move
        "A1",  #1 X
        "C1",  #2 O
        "B1",  #3 X
        "B1",  # O inalid move (move aleady showed on the board)
        "A2",  #4 O
        "C2",  #5 X
        "B2",  #6 O
        "A3",  #7 X
        "C3",  #8 O
        "B3"   #9 X
    ]

    # Mock the input function to return moves in sequence
    with patch('builtins.input', side_effect=moves), \
         patch('deftoe.clear_screen'), \
         patch('deftoe.format_board', return_value="formatted_board"):

        # Run the game function
        result = deftoe.game(first_symbol, second_symbol, board_size, empty_tile, blocked_tile)

        # Assert that the game ends in a draw
        assert result == "draw", "The game should have ended in a draw."

def test_game_blockingTiles_unblockTiles_secondPlayerWin():
    """
    Test the `game` function for a wrong move, hitting non-empty tiles, unblocking non-empty tiles and winning.
    """
    first_symbol = "X"
    second_symbol = "O"
    board_size = 3
    empty_tile = "⬜"
    blocked_tile = "⬛"

    # Define a sequence of moves in the user input format (e.g., 'A1', 'B2')
    # These moves lead to a win of the second player. 
    # Before win there is some hitting of non empty tiles and unblocking of non empty tiles after the board is full.
    # The first input simulates hitting Enter.
    moves = [
        "",     # Simulate hitting Enter at the start
        "A1",  #1 X
        "C1",  #2 O
        "B1",  #3 X
        "A2",  #4 O
        "C2",  #5 X
        "B2",  #6 O
        "A3",  #7 X
        "C2",  #8 O, non-empty tile, blocking
        "B3",  #9 X
        "C3",  #10 O, board is full, Clearing blocked tiles and continuing the game.
        "A1",  #11 X, another non-empty tile, blocking
        "C2",  #12 O, winning move
    ]

    # Mock the input function to return moves in sequence
    with patch('builtins.input', side_effect=moves), \
         patch('deftoe.clear_screen'), \
         patch('deftoe.format_board', return_value="formatted_board"):

        # Run the game function
        result = deftoe.game(first_symbol, second_symbol, board_size, empty_tile, blocked_tile)

        # Assert that the game ends in a draw
        assert result == second_symbol, "The game should have ended in winning move of second player."













