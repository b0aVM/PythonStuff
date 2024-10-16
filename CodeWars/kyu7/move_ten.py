"""
https://www.codewars.com/kata/57cf50a7eca2603de0000090/train/python
"""

s = ("testcase")

def move_ten(st):
    x = ''
    for i in st:
        ascii_code = ord(i)
        chr_ascii = ascii_code + 10
        if chr_ascii > 122:
           x += chr((chr_ascii - 122) + 96)
        else:
            x += chr(chr_ascii)
    return x

print(move_ten(s))