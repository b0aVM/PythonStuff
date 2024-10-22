"""
https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
"""
from operator import index

test = (['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])

def find_needle(haystack):
    idex = "needle"
    for i in haystack:
        if "needle" in haystack:
            index = haystack.index('needle')
        return f"found the needle at position {index}"


print(find_needle(test))

