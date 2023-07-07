import os
from time import sleep

def clear():  # Clears the terminal screen. Makes the app look cleaner if you call this every iteration
    os.system('cls')

def pos_print(str, x, y):  # Better version of print()
    print(f"\033[{y};{x}H", end="")
    print(str, end="")

clear()

sleep(0.5)
pos_print("Don't delete me!", 10, 10)
sleep(0.5)
pos_print("                                       ", 10, 10)
