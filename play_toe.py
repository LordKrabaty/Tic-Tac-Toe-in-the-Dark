"""
Main module for running the Tic Tac Toe game.
This module initializes the game, manages player turns, and tracks scores across multiple games.
"""

from src import deftoe

# Game variables

# Define symbols for players and tiles
player1_symbol = '✖️ '  # Player 1 symbol
player2_symbol = '⭕'   # Player 2 symbol
empty_tile = '⬜'       # Empty or hidden tile symbol
blocked_tile = '⬛'     # Blocked tile symbol
board_size = 3         # Board size, e.g., 3 means 3x3

# Initialize win counters
player1_wins = 0
player2_wins = 0
draws = 0

# Display instructions to players
deftoe.instructions(player1_symbol, player2_symbol)

# Set the starting player
first_symbol = player1_symbol  # Player 1 starts first
second_symbol = player2_symbol

# Ask for game mode
print("Welcome to Tic-Tac-Toe in the Dark!")
print("Choose game mode:")
print("1 - Two players")
print("2 - Play against computer - easy mode")
print("3 - Play against computer - medium mode")
mode = input("Enter 1 or 2 or 3: ").strip()

# Main game loop
while True:
    if mode == "2":
        # Player vs Computer
        result = deftoe.game_vs_random_computer(player1_symbol, player2_symbol, board_size, empty_tile, blocked_tile)
    elif mode == "3":
        # Player vs Computer
        result = deftoe.game_vs_smart_computer(player1_symbol, player2_symbol, board_size, empty_tile, blocked_tile)
    else:
        # Two players
        result = deftoe.game(first_symbol, second_symbol, board_size, empty_tile, blocked_tile)
    
    # Update counters based on the game result
    if result == player1_symbol:
        player1_wins += 1
    elif result == player2_symbol:
        player2_wins += 1
    elif result == "draw":
        draws += 1
    else:
        print("Unexpected result:", result)
    
    # Print the current score
    print(f"\nCurrent Score:")
    print(f"Player 1 ({player1_symbol}): {player1_wins}")
    print(f"Player 2 ({player2_symbol}): {player2_wins}")
    print(f"Draws: {draws}\n")
    
    # Ask players if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("Thanks for playing! Final Score:")
        print(f"Player 1 ({player1_symbol}): {player1_wins}")
        print(f"Player 2 ({player2_symbol}): {player2_wins}")
        print(f"Draws: {draws}")
        break

    # Switch who starts first for the next game

    first_symbol = deftoe.switch_player(first_symbol, player1_symbol, player2_symbol)
    second_symbol = deftoe.switch_player(second_symbol, player1_symbol, player2_symbol)



