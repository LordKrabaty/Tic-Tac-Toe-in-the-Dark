# Tic-Tac-Toe in the Dark

A unique twist on the classic Tic-Tac-Toe game, where the board is partly hidden and players must strategize without always seeing their opponent's moves!

## Features

- **Hidden Moves:** Players do not see the opponent's moves until a non-empty tile is hit.
- **Blocked Tiles:** Hitting a non-empty tile blocks it permanently and reveals all previous moves.
- **Dynamic Board Size:** Easily configurable board size (default is 3x3).
- **Score Tracking:** Tracks wins and draws across multiple games.
- **Replay Option:** Play as many rounds as you like, switching who starts each time.

## How to Play

1. **Start the Game:**  
   Run the main script:
   ```sh
   python play_toe.py
   ```

2. **Instructions:**  
   The game will display instructions and prompt you to start.

3. **Making Moves:**  
   - Enter your move as a column letter followed by a row number (e.g., `A1`, `B2`).
   - If you hit a non-empty tile, it becomes blocked and all moves are revealed.
   - After three moves, all previous moves are revealed (unless a reveal has already occurred).

4. **Winning:**  
   - The first player to get three in a row wins.
   - If the board is full and no one has won, blocked tiles are cleared and the game continues.
   - If the board is full with no blocked tiles and no winner, it's a draw.

5. **Replay:**  
   After each game, you can choose to play again. The starting player alternates each round.

## Project Structure

- `play_toe.py` — Main script to run the game.
- `src/deftoe.py` — Core game logic and helper functions.
- `tests/test_toe.py` — Unit tests for the game logic.
- `readme.md` — This file.

## Running Tests

To run the unit tests:

```sh
pytest tests/test_toe.py
```

## Requirements

- Python 3.7+

No external dependencies are required.

## License

MIT License

---

Enjoy playing Tic-Tac-Toe in the Dark!