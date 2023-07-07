import os  # Needed for decorational functions
import math

state = [0, 0, 0, 0, 0, 0, 0, 0, 0] # list of size 9
winner = ""

def clear():  # Clears the terminal screen. Makes the app look cleaner if you call this every iteration
    os.system('cls')

def pos_print(str, x, y):  # Better version of print()
    print(f"\033[{y};{x}H", end="")
    print(str, end="")

def cell_to_coord(cell): # Math Magic beucase I don't want to hardcode everything :P 
    return ((2 + 4 * ( (cell - 1) % 3) ), (2 * (math.ceil(cell / 3))))

def print_board_state(state): # Prints the board state. Another function because im lazy and over-enginnering everything
    for n in range(0, 9):
        cell = state[n]

        if cell == 1: # Player 1 a.k.a O
            position = cell_to_coord(n + 1)
            pos_print("O", position[0], position[1] + 4)  # The '+3' is the y-offest because the grid is not in the origin

        if cell == -1: # Player 2 a.k.a X
            position = cell_to_coord(n + 1)
            pos_print("X", position[0], position[1] + 4) # The '+3' is the y-offest because the grid is not in the origin


def check_win_conditions():
    x_sum = [0, 0, 0]
    y_sum = [0, 0, 0]
    xy_sum = 0
    neg_xy_sum = 0
    
    for i in range(0, 3):
        x_sum[i] = state[3 * i] + state[(3 * i) + 1] + state[(3 * i) + 2]
    
    for i in range(0, 3):
        y_sum[i] = state[i] + state[3 + i] + state[6 + i]

    xy_sum = state[2] + state[4] + state[6]
    neg_xy_sum = state[0] + state[4] + state[8]

    if 3 in x_sum or 3 in y_sum: return "Player 1 wins!"
    if -3 in x_sum or -3 in y_sum: return "Player 2 wins!"  

    if xy_sum == 3 or neg_xy_sum == 3:   return "Player 1 wins!"
    if xy_sum == 3 or neg_xy_sum == -3:  return "Player 2 wins!"


clear()
#You only need to print all this once.
print("TIC TAC TOE")    
print("Made by Sha")
print("Go have fun")
print("Accepted inputs are 1 to 9. They corespond to the cells from left to right, top to bottom")

print(
    '''
   |   |
---+---+---
   |   |
---+---+---
   |   |
'''
)

player = 1

while True:
    
    print_board_state(state)

    # Check Win Conditions
    winner = check_win_conditions()
         
    if winner: 
        pos_print(winner, 0, 12)
        print("\nPress ENTER to exit the game: ")
        input()
        break

    if all(item != 0 for item in state):
        pos_print("Its a tie!", 0, 12)
        print("\nPress ENTER to exit the game: ")
        input()
        break



    pos_print(f"Player {player}: ", 0, 12)  
    player_input = input()

    if player_input.isspace() or player_input == '': 
        continue

    pos_print(" ", 11, 12)
    try:
        cell_input = int(player_input)
    except ValueError:
        continue

    if cell_input > 9 or cell_input < 1:
        continue

    if player == 1:
        if not state[cell_input - 1]: state[cell_input - 1] = 1   
        player = 2
    else:
        if not state[cell_input - 1]: state[cell_input - 1] = -1
        player = 1    