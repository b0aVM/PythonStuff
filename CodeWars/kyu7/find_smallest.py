"""
https://www.codewars.com/kata/544a54fd18b8e06d240005c0/train/python
"""
from operator import index

test = [5,4,3,2,3],"index"

def find_smallest(numbers, to_return):
    elemen = min(numbers)
    if to_return == "value":
        return min(numbers)
    else:
        return numbers.index(elemen)

print(find_smallest([5,4,3,2,1],"index"))