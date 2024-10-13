"""
https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python
"""

s = (5,5)
def paperwork(n, m):
    while n > 0 and m > 0:
        return m * n
    else:
        return 0

print(paperwork(*s))