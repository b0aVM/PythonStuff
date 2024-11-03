"""
https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
"""

test = ("8 3 -5 42 -1 0 0 -9 4 7 4 -4")

def high_and_low(numbers):
    arr = []
    ans = ''
    list = numbers.split()
    for i in list:
        int_i = int(i)
        arr.append(int_i)
    ans += str(max(arr))
    ans += " "
    ans += str(min(arr))
    return ans

print(high_and_low(test))
