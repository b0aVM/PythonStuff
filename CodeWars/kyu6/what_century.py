"""
https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python
"""


list_of_year = "2154"

def what_century(year: str) -> str:
    def what_century(year):
        year_int = int(year)
        if year_int % 100 == 0:
            century = year_int // 100
        else:
            century = year_int // 100 + 1

        if century % 10 == 1 and century % 100 != 11:
            suffix = 'st'
        elif century % 10 == 2 and century % 100 != 12:
            suffix = 'nd'
        elif century % 10 == 3 and century % 100 != 13:
            suffix = 'rd'
        else:
            suffix = 'th'

        return f"{century}{suffix}"

print(what_century(list_of_year))
