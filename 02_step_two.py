# Step 02 - Making the Logic Visible
# Reeborg's World exercise
#
# In this step I wrote the logic directly in the main file
# so I could follow it better with Step In.

def main():
    while not at_goal():
        move()

        if object_here():
            take()

        elif not object_here():
            while carries_object():
                put()

main()
