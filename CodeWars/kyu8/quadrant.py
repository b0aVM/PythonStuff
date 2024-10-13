"""
https://www.codewars.com/kata/643af0fa9fa6c406b47c5399/train/python
"""

s = [1, 2]

def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4

print(quadrant(*s))