"""
https://www.codewars.com/kata/58fa273ca6d84c158e000052/train/python
"""


test = 12345

def digits(n):
    counter = 0
    digits_count = [int(digit) for digit in str(n)]
    for i in digits_count:
        counter += 1
    return counter


print(digits(test))