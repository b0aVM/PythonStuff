"""
https://www.codewars.com/kata/5830195755f28edad4000081/train/python
"""

test = 2

def get_row(n):
    alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ascii_code = n + 64
    ascii_chr = chr(ascii_code)
    get_row_func = ascii_chr * n
    get_row_func_str = str(get_row_func)
    get_row_func_str_len = len(get_row_func_str)
    alpabet_replace = alpabet[+get_row_func_str_len:]
    if n > 26:
        return alpabet
    else:
        return f"{get_row_func_str}{alpabet_replace}"


print(get_row(test))