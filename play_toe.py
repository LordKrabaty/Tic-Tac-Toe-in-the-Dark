from src import deftoe

# basic variables
# player1 and player2 are the symbols used in the game
player1 = '✖️'
player2 = '⭕'

# game loop
deftoe.game(player1, player2)
    
# Ask to play again
play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again == "yes":
    deftoe.game(player1, player2)
else:
    print("Thanks for playing!")

