from model.player import Player
from random import randint

# Variables

players = []
number_of_rounds = 1
position_end_game = 100

# Shared Methods

def clear_screen():
    print(chr(27) + "[2J")


def dice_roll():
    return randint(1,6)

# Methods

def setup_game():
    number_of_players = int(input("Enter number of players: "))
    i = 0
    
    while i < number_of_players:
        name = input("Player " + str(i +1) +" Name: ")
        players.append(Player(name, 0))
        i+=1

    clear_screen()
    print_game_screen()

def play_game():
    has_won = False
    winning_players = []
    print("")

    for player in players:
        dice_position = dice_roll()

        print(player.name + " rolled " + str(dice_position) + ".")

        player.position += dice_position
        if is_win_position(player.position):
            has_won = True
            winning_players.append(player)
    
    if has_won == True:
        end_game(winning_players)
    else:
        print_game_screen()
       
def end_game(winning_players):
    print("")
    print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
    print("🎉 " + winning_players[0].name + " Won! 🎉")
    print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")

def is_win_position(position):
    if position >= 100:
        return True
    else:
        return False

def print_game_screen():
    global number_of_rounds
    print("+----------+")
    print("  Round " +  str(number_of_rounds))
    print("+----------+")

    # Print Player Status
    for player in players:
        print("")
        print(" Player " + player.name)
        print(" Position : " + str(player.position))

    print("")
    print("+---+-----------+")
    print("| 1 | Roll Dice |")
    print("+---+-----------+")
    print("| 0 | Exit Game |")
    print("+---+-----------+")

    game_command = int(input("Enter Command: "))

    if game_command == 1:
        number_of_rounds+=1
        play_game()

def main():
    print("+-------------------------------+")
    print("|       Python and Ladders      |")
    print("|      < Delacrix Morgan >      |")
    print("+---+---------------------------+")
    print('| 1 | Start Game                |')
    print("+---+---------------------------+")
    print('| 0 | Exit  Game                |')
    print("+-------------------------------+")

    command = input("Enter Command: ")

    setup_game()

    if command == 1:
        setup_game()

main()