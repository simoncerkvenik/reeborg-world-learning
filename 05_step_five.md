# Step 05 - Functions as Small Recipes

## Goal

In this step I practiced using functions.

This task was not really about full automation yet.

It was more about writing small functions and using them like recipes.

---

## Main idea

The robot had to pick strawberries from the garden.

At first, I solved it by writing small functions for repeated movement patterns.

The idea was:

```text
write a small recipe once
call it when needed
repeat the pattern
```

---

## What I noticed

This solution was not fully automatic.

The robot did not really decide everything by itself.

I still had to tell it the movement pattern.

But the code became cleaner because I used functions instead of writing all commands directly in one long block.

---

## Example idea

Instead of writing all moves directly in the main program, I could create functions like:

```python
def pick_two_berries_from_left():
    move()
    turn_left()
    move()
    take()
    move()
    take()
```

And then call the function when needed.

---

## What I learned

In this step I learned that a function can be used as a small named recipe.

A function helps me group commands together.

This makes the code easier to read and easier to reuse.

The main lesson was:

```text
functions can organize repeated steps
```

This step was not full automation, but it helped me understand how to split a bigger task into smaller parts.
