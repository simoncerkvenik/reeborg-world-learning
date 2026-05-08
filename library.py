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

def front_is_wall():
    if wall_in_front() and right_is_clear():
        turn_right()
    elif wall_in_front() and not right_is_clear():
        turn_left()

def finish():
    if at_goal() and carries_object():
        u_turn()
        move()
        put()
        u_turn()
        move()
