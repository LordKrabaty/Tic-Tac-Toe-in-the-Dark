from src import deftoe

# game variables

player1 = '✖️' # Player 1 symbol
player2 = '⭕' # Player 2 symbol
empty_tile = '⬜' # Empty tile symbol
boad_size = 3 # board size, 3 means 3x3 etec

# instuctions
deftoe.instructions(player1, player2) 

# game loop
deftoe.game(player1, player2, boad_size, empty_tile)
    
# Ask to play again
play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again == "yes":
    deftoe.game(player1, player2, empty_tile)
else:
    print("Thanks for playing!")

