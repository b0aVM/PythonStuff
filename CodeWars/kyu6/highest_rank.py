"""
https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python
"""
from collections import Counter

tuple_test = [12, 10, 8, 12, 7, 6, 4, 10, 10]

def highest_rank(arr):
    sort_arr = sorted(arr)
    sort_arr_rev = sort_arr.reverse()
    count = Counter(sort_arr)
    most_common_element, most_common_count, = count.most_common(1)[0]
    return most_common_element

print(highest_rank(tuple_test))