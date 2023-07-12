"""
Description: Implementation of Binary search
write a binary search function with an iterative approach (loops).
inputs:
1. a Python list to search through, and
2. The value we're searching for.

Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list

Complexity: O(log(n))

"""

import math


def binary_search(mylist, value):
    start = 0
    end = len(mylist) - 1
    while start <= end:
        mid = math.floor((start + end) / 2)
        if mylist[int(mid)] == value:
            return mid
        elif value > mylist[int(mid)]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# Test cases
test_list = [2, 3, 8, 15, 23, 29, 45, 80]
val1 = 12
val2 = 80
print(binary_search(test_list, val1))
print(binary_search(test_list, val2))
