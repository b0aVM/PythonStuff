"""
https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
"""

test = 416419518416

def descending_order(num):
    result = ""
    split = [int(numbers) for numbers in str(num)]
    sorted_num = sorted(split)
    reverse = sorted_num.reverse()
    for i in sorted_num:
        result += str(i)
    return int(result)

print(descending_order(test))