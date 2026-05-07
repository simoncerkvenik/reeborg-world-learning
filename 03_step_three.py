# Step 03 - Leaving the Goal First
# Reeborg's World exercise

def main():
    move()

    while not at_goal():
        move()

        if wall_in_front():
            turn_left()

main()
