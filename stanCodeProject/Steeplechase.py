"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        while front_is_clear():
            move()
        jump()

def jump():
    up()
    cross()
    down()

def up():
    if not front_is_clear():
        turn_left()
        move()
        turn_right()

def cross():
    move()
    turn_right()

def down():
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    for i in range(3)
        turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
