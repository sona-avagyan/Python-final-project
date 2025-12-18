from src.utils import is_in_board, neighbors, empty_board, print_board
import sys

ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

def validate_ship(ship, board):
    #ship is a list of tuples of coordinates

    #if ship is empty
    if len(ship) == 0:
        return False
    
    #if ship is in board
    for x, y in ship:
        if not is_in_board(x, y):
            return False
        
    #if ship is on the axis
    x0 = ship[0][0]
    y0 = ship[0][1]

    same_x = True
    same_y = True

    for cell in ship:
        if cell[0] != x0:
            same_x = False
        if cell[1] != y0:
            same_y = False
        
    if not same_x and not same_y:
        return False
    
    #if ship is solid
    sorted_ship = sorted(ship)

    for i in range(len(ship)-1):
        x1 = sorted_ship[i][0]
        y1 = sorted_ship[i][1]
        x2 = sorted_ship[i+1][0]
        y2 = sorted_ship[i+1][1]

        if abs(x2-x1) + abs(y2-y1) != 1:
            return False
        
    #if ship touches other ship
    for cell in ship:
        x = cell[0]
        y = cell[1]

        for neighbor in neighbors(x, y):
            new_x = neighbor[0]
            new_y = neighbor[1]
            
            #if there is already ship in neighbor cell and the cell is not in ship
            if board[new_x][new_y] == "S" and (new_x, new_y) not in ship:
                return False
            
    return True


def input_player_ships():
    board = empty_board()
    ships = []

    for size in ship_sizes:
        print("Put a ship the size of ", size)
        valid = False

        while valid == False:
            ship = []
            #input of each cell of ship and append it into ship
            for i in range(size):
                while True:
                    input_ = input(f"Give coordinates {i+1} (x, y) or 'exit' to quit: ").strip() #remove extra spaces 
                    if input_.lower() == "exit":
                        print("Exiting")
                        sys.exit()
                    try:
                        x_str, y_str = input_.split() #split into list of strings
                        x = int(x_str)
                        y = int(y_str)
                        ship.append((x, y))
                        break
                    except ValueError:
                        print("Wrong input")

            if validate_ship(ship, board):
                #adding ship
                for cell in ship:
                    x = cell[0]
                    y = cell[1]
                    board[x][y] = "S"

                ships.append(ship)
                valid = True
                print("Ship added")
                print_board(board, hide_ships=False)
            else:
                print("Wrong ship placement")

    return board, ships

            
