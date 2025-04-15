from src import deftoe

# game variables

player1 = '✖️' # Player 1 symbol
player2 = '⭕' # Player 2 symbol

# game loop
deftoe.game(player1, player2)
    
# Ask to play again
play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again == "yes":
    deftoe.game(player1, player2)
else:
    print("Thanks for playing!")

