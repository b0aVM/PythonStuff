"""
https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python
"""

s = [1, 2, 3]

def grow(arr):
    x = 1
    for i in arr:
        x *= i
    return x

print(grow(s))