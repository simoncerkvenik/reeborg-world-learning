# Step 03 - Leaving the Goal First

## Goal

In this step I learned that the robot can start already on the goal.

Because of that, this loop does not start immediately:

```python
while not at_goal():
```

The robot is already at the goal, so `at_goal()` is true.

That means `not at_goal()` is false.

---

## First idea

First I used only:

```python
def main():
    move()

main()
```

The idea was simple:

```text
first move away from the goal
```

This was important because I had to move the robot away from the goal first.

Only after that could I use the goal as the stopping point.

---

## Final logic

Then I added the loop:

```python
def main():
    move()

    while not at_goal():
        move()

        if wall_in_front():
            turn_left()

main()
```

The logic was:

```text
first move away from the goal

while the robot is not at the goal:
    move forward

    if there is a wall in front:
        turn left
```

---

## What I learned

The first `move()` had to be outside the loop.

That move changed the robot's position.

After that, the robot was no longer on the goal, so the loop could start.

The main lesson was:

```text
sometimes I first have to change the robot's state
before a loop can work correctly
```

In this step I learned:

```text
move away first
then use the goal as the stopping condition
```
