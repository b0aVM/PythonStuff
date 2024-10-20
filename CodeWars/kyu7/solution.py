"""
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
"""

test = ("gay", "ay")

def solution(text, ending):
    End = len(ending)
    Text = text[-End:]
    if ending in Text:
        return True
    else:
        return False


print(solution("gay", "ay"))