"""
https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
"""

s = [(45, 12),(55,21),(19, -2),(104, 20)]

def open_or_senior(data):

    result = []

    for i in data:
        if i[0] >= 55 and i[1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

print(open_or_senior(s))