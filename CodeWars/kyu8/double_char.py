'''
https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
'''

s = ("String")

def double_char(s):
    x = ''
    for i in s:
       x += i * 2
    return x

print(double_char(s))