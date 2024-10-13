"""
https://www.codewars.com/kata/56f6ad906b88de513f000d96/train/pythonw
"""
s = (10000, True)

def bonus_time(salary, bonus):
    #your code here
    if bonus == True:
        return "$" + str(salary * 10)
    else:
        return "$" + str(salary)

print(bonus_time(*s))