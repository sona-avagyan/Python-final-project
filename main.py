from src.ship_input import input_player_ships
from src.utils import save_ships_to_csv, print_board, empty_board
from src.bot_generation import generate_bot_ships
from src.gameplay import play_game

def main():
    print("Game is starting")
    empty_board_ = empty_board()
    print_board(empty_board_)

    #Player ships
    player_board, player_ships = input_player_ships()
    save_ships_to_csv(player_ships, "data/player_ships.csv")

    #Bot ships
    bot_board, bot_ships = generate_bot_ships()
    save_ships_to_csv(bot_ships, "data/bot_ships.csv")

    #Show player board
    print("Your ships:")
    print_board(player_board)

    #Start game loop
    play_game(player_board, bot_board, player_ships, bot_ships)

if __name__ == "__main__":
    main()

