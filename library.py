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

def pick_two_berries_from_left():
    move()
    turn_left()
    move()
    take()
    move()
    take()
    u_turn()
    move()
    move()
    while carries_object():
        put()
    turn_left()  
    
def pick_two_berries_from_right(): 
    move()
    turn_right()
    move()
    take()
    move()
    take()
    u_turn()
    move()
    move()
    turn_right()
    while carries_object():
        put()
            
