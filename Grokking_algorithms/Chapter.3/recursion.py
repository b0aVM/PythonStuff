"""

Recursion

• Recursion is when a function calls itself.
• Every recursive function has two cases: the base case
and the recursive case.

"""

def countdown(i):
    print(i)
    countdown(i-1)

print(countdown(1))

def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i -1)

print(countdown(100))

# The call stack with recursion

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(3))

