from src import deftoe

# game variables

# Define symbols for players and empty tile
player1 = '✖️ '  # Player 1 symbol
player2 = '⭕'   # Player 2 symbol
empty_tile = '⬜' # Empty tile symbol
board_size = 3   # Board size, 3 means 3x3

# Initialize win counters
player1_wins = 0
player2_wins = 0
draws = 0

# Instructions  
deftoe.instructions(player1, player2)

# who starts first
first_player_symbol = player1
second_player_symbol = player2

# Main game loop
while True:
    # Play the game and get the result
    result = deftoe.game(first_player_symbol, second_player_symbol, board_size, empty_tile)
    
    # Update counters based on the game result
    if result == player1:
        player1_wins += 1
    elif result == player2:
        player2_wins += 1
    elif result == "draw":
        draws += 1
    else:
        print("Unexpected result:", result)
    
    # Print the current score
    print(f"Score - Player 1: {player1_wins}, Player 2: {player2_wins}, Draws: {draws}")
    
    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
    # switching players
    first_player_symbol = player2 if first_player_symbol == player1 else player1
    second_player_symbol = player1 if first_player_symbol == player2 else player2


