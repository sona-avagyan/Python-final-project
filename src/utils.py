import csv

board_size = 10

# S - ship
# . - nothing
# X - hit
# * - miss

#create empty board
def empty_board():
    board = []
    for _ in range(board_size):
        row = []
        for _ in range(board_size):
            row.append(".")
        board.append(row)
    return board

#check if coordinates are in board
def is_in_board(x, y):
    return 0<=x<board_size and 0<=y<board_size

#return a list of neighbors
def neighbors(x, y):
    res = []
    for x_ in [-1, 0, 1]: #directions
        for y_ in [-1, 0, 1]:
            if x_ == 0 and y_ == 0:
                continue
            new_x = x + x_
            new_y = y + y_
            if is_in_board(new_x, new_y):
                res.append((new_x, new_y))
    return res

#print board
def print_board(board, hide_ships = False): #if sym is ship, then make it .
    print("  0 1 2 3 4 5 6 7 8 9") # column numbers
    for i in range(board_size):
        print(i, end=" ") #row numbers
        for j in range(board_size):
            cell = board[i][j]

            if hide_ships and cell == "S":
                print(".", end=" ")
            else:
                print(cell, end=" ")
        
        print()

#save ships to csv file
def save_ships_to_csv(ships, filename):
    #each row in csv is one ship cell
    with open(filename, "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(["ship_id", "x", "y"])
        ship_id = 0
        for ship in ships:
            for cell in ship:
                x = cell[0]
                y = cell[1]
                writer.writerow([ship_id, x, y])
            ship_id +=1
        
