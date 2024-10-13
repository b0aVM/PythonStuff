"""
https://www.codewars.com/kata/5bb904724c47249b10000131/train/python
"""

s = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']

def points(games):
    counter = 0
    for i in games:
        x = (i[0])
        y = (i[2])
        if x > y:
            counter += 3
        elif x < y:
            counter += 0
        elif x == y:
            counter += 1
    return counter

print(points(s))
