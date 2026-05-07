# Step 02 - Making the Logic Visible

## Goal

In this step I started building more automatic logic in Reeborg's World.

First I tried to use `library.py`, but for learning it was harder, because I could not follow the logic clearly with Step In.

So I removed:

```python
from library import *
```

and wrote the logic directly in the main file.

This helped me see what the robot was doing line by line.

---

## First try

First I tried this:

```python
def main():
    while not at_goal():
        move()
        take()

main()
```

My idea was simple:

```text
while the robot is not at the goal:
    move
    take
```

But this caused an error.

The robot came to a place where there was no object, but I still told it to use:

```python
take()
```

So I learned that I cannot use `take()` blindly.

The robot must check first if an object is there.

---

## Second try

Then I tried this:

```python
def main():
    while not at_goal():
        move()
        take()
        while not object_here():
            put()

main()
```

But this was also wrong.

After `take()`, the object is not on the square anymore.

So this became true:

```python
while not object_here():
```

Then the robot used `put()` right away.

So it picked up the object and put it back down immediately.

I learned that after `take()`, the square changes.

---

## Third try

Then I tried to put before taking:

```python
def main():
    while not at_goal():
        move()
        if not object_here():
            put()
        take()
        
main()
```

This also had a problem.

The robot could put an object down, but then `take()` came right after it.

So it could take back what it just put down.

I learned that the order of commands matters a lot.

---

## Fourth try

Then I tried using `if` and `elif`:

```python
def main():
    while not at_goal():
        move()

        if object_here():
            take()

        elif not object_here():
            while carries_object():
                put()
        
main()
```

This worked better.

Now the robot had a choice:

```text
if there is an object:
    take it

elif there is no object:
    if the robot is carrying something:
        put it down
```

The important part was `elif`.

With `elif`, the robot does not do everything at once.

It chooses one action.

---

## What I learned

In this step I learned that automation is not only about writing commands.

The robot must check the situation first.

Important lessons:

```text
do not take blindly
do not put immediately after take
do not take immediately after put
use if and elif so the robot chooses one action
```

The biggest lesson was:

```text
the order of logic matters
```

This step helped me understand how `while`, `if`, `elif`, `object_here()`, `take()`, `put()`, and `carries_object()` work together.# Step 02 - Making the Logic Visible

## Goal

In this step I started building more automatic logic in Reeborg's World.

First I tried to use `library.py`, but for learning it was harder, because I could not follow the logic clearly with Step In.

So I removed:

```python
from library import *
```

and wrote the logic directly in the main file.

This helped me see what the robot was doing line by line.

---

## First try

First I tried this:

```python
def main():
    while not at_goal():
        move()
        take()

main()
```

My idea was simple:

```text
while the robot is not at the goal:
    move
    take
```

But this caused an error.

The robot came to a place where there was no object, but I still told it to use:

```python
take()
```

So I learned that I cannot use `take()` blindly.

The robot must check first if an object is there.

---

## Second try

Then I tried this:

```python
def main():
    while not at_goal():
        move()
        take()
        while not object_here():
            put()

main()
```

But this was also wrong.

After `take()`, the object is not on the square anymore.

So this became true:

```python
while not object_here():
```

Then the robot used:

```python
put()
```

right away.

So it picked up the object and put it back down immediately.

I learned that after `take()`, the square changes.

---

## Third try

Then I tried to put before taking:

```python
def main():
    while not at_goal():
        move()
        if not object_here():
            put()
        take()
        
main()
```

This also had a problem.

The robot could put an object down, but then `take()` came right after it.

So it could take back what it just put down.

I learned that the order of commands matters a lot.

---

## Fourth try

Then I tried using `if` and `elif`:

```python
def main():
    while not at_goal():
        move()

        if object_here():
            take()

        elif not object_here():
            while carries_object():
                put()
        
main()
```

This worked better.

Now the robot had a choice:

```text
if there is an object:
    take it

elif there is no object:
    if the robot is carrying something:
        put it down
```

The important part was `elif`.

With `elif`, the robot does not do everything at once.

It chooses one action.

---

## Important detail

Another important part was this:

```python
while carries_object():
    put()
```

This means:

```text
if the robot is carrying something,
put it down
```

This was important because the robot should not try to put something down if it is not carrying anything.

So the robot first checks:

```text
am I carrying something?
```

Only then it uses:

```python
put()
```

Without this check, the robot could try to put something down even when it has nothing to put.

So the logic became:

```text
no object here + carrying something = put
no object here + carrying nothing = do not put
```

---

## What I learned

In this step I learned that automation is not only about writing commands.

The robot must check the situation first.

Important lessons:

```text
do not take blindly
do not put immediately after take
do not take immediately after put
check if the robot is carrying something before put
use if and elif so the robot chooses one action
```

The biggest lesson was:

```text
the order of logic matters
```

This step helped me understand how `while`, `if`, `elif`, `object_here()`, `take()`, `put()`, and `carries_object()` work together.
