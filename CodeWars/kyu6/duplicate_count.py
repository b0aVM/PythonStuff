"""
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
"""
from collections import Counter

test = "abcdeaa"

def duplicate_count(text):
    modified_text = text.lower()
    list = [x for x in modified_text]
    counter = Counter(list)
    value = counter.values()
    count = 0
    for i in value:
        if i != 1:
            count += 1
        else:
            pass
    return count




print(duplicate_count(test))