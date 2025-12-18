# Python-final-project
Battleship Game 

1. How input format works
A ship is a list of cells, each of which is in turn a tuple of the x y coordinates of each cell.
Сoordinates are numbers from 0 to 9.
To interact with a cell, the user enters its x y coordinates in one input.

2. How you validate ship placements
All these checks are performed in src/ship_input.py in the validate_ship function.

This checks
- Whether the ship is empty or not.
- Whether it is within the board's boundaries.
- It must be consistently horizontal or vertical.
- Whether it is not touching other ships, even diagonally.

3. How update and display the game state
Two boards are used: the player's and the bot's.
After every move, the board is updated:  
  - `"X"` for hit  
  - `"*"` for miss  
Two sets are used to track previous shots:  
  - `player_hits` for player's shots  
  - `bot_hits` for bot's shots  
Destroyed ships’ surrounding cells are automatically marked as `"*"` (miss).  
The CSV file `data/game_state.csv` stores each turn.

Display
- The player’s board shows all ships, hits, and misses.
- The bot’s board hides ships, showing only hits and misses.
- Updated boards are printed in the console after each turn.

4. Any design decisions or trade-offs
- The field is stored as a regular list, shots are stored in sets.
- The game is played in the terminal, without graphics.
- Divided into modules: gameplay, bot, ship input, utilities.
- No graphical interface.
- Output only in the console.
