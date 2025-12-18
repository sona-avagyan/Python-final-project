import sys
import csv
from src.utils import print_board, is_in_board, neighbors
import random

def ship_destroyed(ship, board):
    for cell in ship:
        x = cell[0]
        y = cell[1]

        if board[x][y] == "S":
            return False
        
    return True

def all_ships_destroyed(ships, board):
    for ship in ships:
        for cell in ship:
            x = cell[0]
            y = cell[1]

            if board[x][y] == "S":
                return False
            
    return True

def mark_neighbors(ship, board):
    for cell in ship:
        x = cell[0]
        y = cell[1]

        surrounding = neighbors(x, y)

        for neighbor in surrounding:
            new_x = neighbor[0]
            new_y = neighbor[1]

            if board[new_x][new_y] == ".":
                board[new_x][new_y] = "*"

#making string for csv
def board_to_string(board):
    result = ""

    for row in board:
        for cell in row:
            result += cell
        result += "|"

    return result

def get_ship_orientation(hits):
    if len(hits) < 2:
        return None
    (x1, y1), (x2, y2) = hits[0], hits[1]
    if x1 == x2:
        return "H" 
    else:
        return "V"

def save_game_state(turn, player_move, bot_move, player_board, bot_board):
    with open("data/game_state.csv", "a", newline="") as f:
        writer = csv.writer(f)

        player_board_str = board_to_string(player_board)
        bot_board_str = board_to_string(bot_board)

        writer.writerow([
            turn,
            player_move,
            bot_move,
            player_board_str,
            bot_board_str
        ])


def bot_choose_target(player_board, bot_hits, last_hits):
    board_size = 10

    if last_hits:
        orientation = get_ship_orientation(last_hits)
        for x0, y0 in last_hits:
            directions = []
            if orientation == "H":
                directions = [(0,1), (0,-1)]
            elif orientation == "V":
                directions = [(1,0), (-1,0)]
            else:
                directions = [(0,1), (0,-1), (1,0), (-1,0)]

            for dx, dy in directions:
                nx, ny = x0 + dx, y0 + dy
                if 0 <= nx < board_size and 0 <= ny < board_size:
                    if (nx, ny) not in bot_hits:
                        return nx, ny
                    
    while True:
        b_x = random.randint(0,9)
        b_y = random.randint(0,9)
        if (b_x, b_y) not in bot_hits:
            return b_x, b_y






def play_game(player_board, bot_board, player_ships, bot_ships):
    turn = 1
    player_hits = set() 
    bot_hits = set()     
    bot_last_hits = []  

    while True:
        print(f"\nTurn {turn}")
        print("Your turn")
        
        while True:
            input_ = input("Enter coordinates to shoot (x y) or 'exit' to quit: ").strip()
            if input_.lower() == "exit":
                print("Game ended")
                sys.exit()
            try:
                x_str, y_str = input_.split()
                x = int(x_str)
                y = int(y_str)
                if not is_in_board(x, y):
                    print("Out of board")
                    continue
                if (x, y) in player_hits:
                    print("You already shot here")
                else:
                    break
            except:
                print("Wrong input")

        if bot_board[x][y] == "S":
            print("Hit")
            bot_board[x][y] = "X"

            for ship in bot_ships:
                if (x, y) in ship:
                    if ship_destroyed(ship, bot_board):
                        mark_neighbors(ship, bot_board)
                    break
        else:
            print("Miss")
            bot_board[x][y] = "*"

        player_hits.add((x, y))
        print("\nBot board (hidden ships):")
        print_board(bot_board, hide_ships=True)

        if all_ships_destroyed(bot_ships, bot_board):
            print("\nYOU WIN!")
            return


        print("\nBot's turn")
        bx, by = bot_choose_target(player_board, bot_hits, bot_last_hits)

        if player_board[bx][by] == "S":
            print(f"Bot hit at ({bx},{by})!")
            player_board[bx][by] = "X"
            bot_last_hits.append((bx, by))
          
            for ship in player_ships:
                if (bx, by) in ship:
                    if ship_destroyed(ship, player_board):
                        mark_neighbors(ship, player_board)
                        
                        bot_last_hits = []
                    break
        else:
            print(f"Bot miss at ({bx},{by})")
            player_board[bx][by] = "*"

        bot_hits.add((bx, by))

        print("\nYour board:")
        print_board(player_board)

        if all_ships_destroyed(player_ships, player_board):
            print("\nBOT WINS!")
            return

        turn += 1

