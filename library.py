# Reeborg helper library
# This file contains reusable logic for Reeborg's World.

def walk():
    while front_is_clear():
        move()

def turn_wright():
    turn_left()
    turn_left()
    turn_left()

def u_turn():
    turn_left()
    turn_left()


