# Step 05 - Main program
# Reeborg's World exercise

from library import *

def main():
    pick_two_berries_from_left()
    pick_two_berries_from_right()
    pick_two_berries_from_left()
    pick_two_berries_from_right()

    while not at_goal():
        move()
    
main()
