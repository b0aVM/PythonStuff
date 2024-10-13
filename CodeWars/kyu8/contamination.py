'''
https://www.codewars.com/kata/596fba44963025c878000039/train/python
'''

def contamination(text, char):
    j = ""
    for i in text:
        j += char
    return j

con = ("abc", "z")

print(contamination(*con))