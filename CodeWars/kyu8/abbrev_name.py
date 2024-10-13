'''
https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python
'''

def abbrev_name(name):
    y = ""
    x = name.split(" ")
    y += x[0][0] + "." + x[1][0]
    return y.upper()

s = 'samm harrys'
print(abbrev_name(s))