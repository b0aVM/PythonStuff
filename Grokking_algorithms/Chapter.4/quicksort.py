"""

Quicksort

• D&C works by breaking a problem down into smaller and smaller
pieces. If you’re using D&C on a list, the base case is probably an
empty array or an array with one element.
• If you’re implementing quicksort, choose a random element as the
pivot. The average runtime of quicksort is O(n log n)!
• The constant in Big O notation can matter sometimes. That’s why
quicksort is faster than merge sort.
• The constant almost never matters for simple search versus binary
search, because O(log n) is so much faster than O(n) when your list
gets big.

"""


# You have to add up all the numbers and return the total. It’s pretty easy
# to do this with a loop:

def sum(arr):
    if len(arr) == 1:
        return arr[0]
    piv = arr[0]
    less = [x for x in arr if x < piv]
    more = [x for x in arr if x > piv]
    return piv + sum(more)

print(sum([2,4,6]))

def quicksort(array):
    if len(array) < 2:
        return array    #Base case: arrays with 0 or 1 element are already “sorted.”
    else:
        pivot = array[0] #Recursive case
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot] #Sub-array of all the elements less than the pivot
        return quicksort(less) + [pivot] + quicksort(greater) #Sub-array of all the elements greater than the pivot

print(quicksort([10, 5, 2, 3]))