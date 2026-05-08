# Step 04 - Helper Functions and Flower Logic
# Reeborg's World exercise

from library import *

def main():
    while not at_goal():
        move()

        if wall_in_front() and carries_object() and right_is_clear() and not at_goal():
            put()

        elif object_here():
            take()

        finish()
        front_is_wall()

main()
