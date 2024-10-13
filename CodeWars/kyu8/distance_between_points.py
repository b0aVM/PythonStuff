"""
https://www.codewars.com/kata/58dced7b702b805b200000be/train/python
"""
from os.path import split


def distance_between_points(a, b):
    if a.y == b.y and a.x == b.x:
        return 0
    return ((a.y - b.y)**2 + (a.x - b.x)**2)**0.5

