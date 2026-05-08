# Step 04 - Helper Functions and Flower Logic

## Goal

In this step I started using `library.py` again.

This time I used the library only for small helper functions.

The main logic stayed visible in the main file, but repeated actions like turning were moved into the library.

---

## Library helpers

First I added turning helpers:

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def u_turn():
    turn_left()
    turn_left()
```

Then I added wall logic:

```python
def front_is_wall():
    if wall_in_front() and right_is_clear():
        turn_right()
    elif wall_in_front() and not right_is_clear():
        turn_left()
```

The idea was simple:

```text
if there is a wall in front and the right side is clear:
    turn right

if there is a wall in front and the right side is not clear:
    turn left
```

---

## Importing the library

In the main file I used:

```python
from library import *
```

The `*` means that everything from `library.py` is imported.

This allowed me to call my helper functions directly.

---

## First working movement logic

With the wall helper, the main program became cleaner:

```python
from library import *

def main():
    while not at_goal():
        move()
        front_is_wall()
        
main()
```

This worked because the robot could move and react to walls.

The logic was:

```text
move forward
if there is a wall, turn
repeat until the goal
```

---

## Adding flower pickup

Then I added flower pickup:

```python
from library import *

def main():
    while not at_goal():
        move()
        front_is_wall()

        if object_here():
            take()
        
main()
```

This allowed the robot to collect flowers on the path.

---

## Flower helper

Then I moved the flower logic into `library.py`:

```python
def flower():
    if object_here():
        take()
```

Now I could call:

```python
flower()
```

instead of writing this every time:

```python
if object_here():
    take()
```

---

## Problem: putting and taking back

Then I tried to put the flower down when the robot was carrying one:

```python
from library import *

def main():
    while not at_goal():
        move()

        if wall_in_front() and carries_object() and right_is_clear():
            put()

        front_is_wall()
        flower()
        
main()
```

This created a problem.

After `put()`, the flower was on the ground again.

Then `flower()` ran right after it.

Because `flower()` checks `object_here()`, the robot took back the same flower it had just put down.

So the robot was doing:

```text
put
take again
```

That was not the goal.

---

## Changing the order

Then I tried moving `flower()` before the put logic:

```python
from library import *

def main():
    while not at_goal():
        move()
        flower()

        if wall_in_front() and carries_object() and right_is_clear():
            put()

        front_is_wall()
        
main()
```

But this also had a problem.

The robot picked up the flower first.

Then, in the same loop, it checked the wall condition and put the flower down immediately.

So again the order was not enough.

The real problem was that the robot could still do two things in the same loop.

---

## Fix: if and elif

The fix was to use `if` and `elif`.

```python
from library import *

def main():
    while not at_goal():
        move()

        if wall_in_front() and carries_object() and right_is_clear():
            put()

        elif object_here():
            take()

        front_is_wall()
        
main()
```

This worked much better.

The logic became:

```text
if the robot has to put the flower down:
    put it down

elif there is a flower here:
    take it
```

The important part was `elif`.

With `elif`, the robot does not do both actions in the same loop.

It chooses one action.

```text
put OR take
not both at the same time
```

---

## Goal problem

Then I found another problem.

In one world, the robot tried to put the flower down near the goal.

So I added:

```python
and not at_goal()
```

The condition became:

```python
if wall_in_front() and carries_object() and right_is_clear() and not at_goal():
    put()
```

This means:

```text
put the flower down only if the robot is carrying something
and is not already at the goal
```

---

## Finish helper

Then I added a finish helper in `library.py`.

I named it:

```python
def finish():
    if at_goal() and carries_object():
        u_turn()
        move()
        put()
        u_turn()
        move()
```

The idea was:

```text
if the robot reaches the goal while still carrying a flower:
    turn around
    move back
    put the flower down
    turn around again
    return to the goal
```

At first I called `finish()` at the very end.

That did not work well, because the robot turned left before finishing.

Then I moved `finish()` one step earlier, before the wall helper.

After that, everything worked.

---

## Final main logic

```python
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
```

---

## What I learned

In this step I learned that order matters a lot.

It was not enough to just write the right commands.

I had to place them in the right order.

Important lessons:

```text
helper functions can keep the main code cleaner

put and take must not happen in the same loop

elif helps the robot choose only one action

not at_goal() prevents putting at the wrong place

finish logic must happen before wall turning
```

The biggest lesson was:

```text
the robot does exactly what I write,
not what I mean
```

This step helped me understand how helper functions, conditions, and order of logic work together.
