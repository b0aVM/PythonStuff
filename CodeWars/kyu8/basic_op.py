"""
https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
"""

s = ('+', 4, 7)

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    if operator == "-":
        return value1 - value2
    if operator == "*":
        return value1 * value2
    if operator == "/":
        return value1 / value2

print(basic_op(*s))