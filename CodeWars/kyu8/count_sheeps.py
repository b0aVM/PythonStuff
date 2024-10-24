"""
https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
"""

array1 = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]

def count_sheeps(sheep):
    counter = 0
    for i in sheep:
        if i == True:
            counter += 1
        else:
            counter += 0
    return counter

print(count_sheeps(array1))