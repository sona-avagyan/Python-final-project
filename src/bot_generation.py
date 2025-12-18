from src.utils import empty_board
from src.ship_input import validate_ship
import random

ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

def generate_bot_ships():
    board = empty_board()
    ships = []

    for size in ship_sizes:
        valid = False
        while not valid:
            orientation = random.choice(["H", "V"]) #horizontal or vertical
            if orientation == "H":
                x = random.randint(0, 9)
                y = random.randint(0, 10 - size)
                ship = [(x, y + i) for i in range(size)]
            else:
                x = random.randint(0, 10 - size)
                y = random.randint(0, 9)
                ship = [(x + i, y) for i in range(size)]

            if validate_ship(ship, board):
                for x, y in ship:
                    board[x][y] = "S"
                ships.append(ship)
                valid = True

    return board, ships
