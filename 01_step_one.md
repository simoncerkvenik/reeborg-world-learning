# Step 01 - From Manual Commands to Automation

## Goal

The goal of this step is to document how I started thinking about automation in Reeborg's World.

At first, I was thinking only in simple manual commands.

---

## First idea - manual movement

My first idea was simply:

```python
move()
move()
move()
move()
```

This means that the robot moves forward four times.

This works only if the world is always exactly the same.

The problem with this approach is that the robot does not check anything:

- it does not check if there is a wall
- it does not check if there is an object
- it does not know when to stop
- it only follows fixed commands

So this was not real automation yet.

It was just a manual path written as code.

---

## How my thinking changed

Then I used artificial intelligence to help me see an automatic version of the code.

Only after seeing that automatic code, I started to understand the real idea:

The robot should not only receive fixed commands.

The robot needs logic.

That means I have to give it rules, such as:

```text
check the situation
decide what to do
repeat until the task is finished
```

This was an important moment in my learning.

I realized that programming is not only about writing commands one after another.

Programming is about creating logic that can react to the situation.

---

## Manual solution vs automatic solution

Manual solution:

```text
Do this exact command.
Then this exact command.
Then this exact command.
```

Automatic solution:

```text
Check what is happening.
Choose the correct action.
Repeat until the task is finished.
```

---

## What the robot can check

The robot does not understand the whole world like a human.

It can only check simple conditions:

```python
front_is_clear()
wall_in_front()
right_is_clear()
object_here()
carries_object()
at_goal()
```

These checks are the beginning of automation.

Instead of only telling the robot:

```text
move here
move there
take this
put that
```

I started thinking:

```text
What does the robot see right now?
What is the correct action in this situation?
When should the robot stop?
```

---

## First lesson

Automation starts when I stop writing only fixed steps and start writing rules.

The first real change in my thinking was this:

```text
Do not only control the robot.
Teach the robot how to decide.
```

This is the beginning of programming logic.

---

## Using a library

After the first manual steps, I also started using a small library.

The idea is that I can write useful logic once in the library, and then call it from the main program.

In the main file I can import everything from the library with:

```python
from library import *
```

This helps me keep the code cleaner.

Instead of writing the same logic again and again, I can create functions in the library and reuse them.

For example, if I create a helper function in the library, I can later call it from the main program.

This is another step toward automation:

```text
write the logic once
save it in the library
call it when needed
```

This makes the program easier to read, easier to test, and easier to improve.

---

## My first logic

My first logic in the library was:

```python
def walk():
    while front_is_clear():
        move()
```

This function means:

```text
while the path in front is clear,
keep moving forward
```

Before this, I was writing fixed commands like:

```python
move()
move()
move()
move()
```

With `walk()`, the robot starts using a rule instead of a fixed number of steps.

This was my first real automation function.

---

## What this step taught me

This step taught me that programming is not only about writing commands.

At first, I was controlling the robot manually.

Later, I started thinking about how the robot can make simple decisions based on the situation.

The important change was:

```text
from fixed commands
to reusable logic
```

This was the beginning of automation in my Reeborg learning process.
