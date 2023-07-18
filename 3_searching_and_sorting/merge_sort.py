"""
Description: Implementation of Merge sort algorithm
Input: A sequence of n elements <a1, a2, ..., an>
Output: A permutation <a1', a2', ..., an'> of the input such that
a1'<= a2' <= ... <=an'

Time Complexity: O(n log(n))
Space Complexity: O(n) because we copy all elements to new array at
each iteration (assuming that we get rid of the space after each iteration

"""

import math


def merge(arr, begin, mid, end):
    left_size = mid - begin + 1
    right_size = end - mid

    left_arr = [0] * left_size
    right_arr = [0] * right_size

    for i in range(0, left_size):
        left_arr[i] = arr[begin + i]

    for j in range(0, right_size):
        right_arr[j] = arr[mid + j + 1]

    i, j, k = 0, 0, begin

    while i < left_size and j < right_size:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < left_size:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < right_size:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, begin, end):
    if begin < end:
        mid = math.floor((begin + end) / 2)

        merge_sort(arr, begin, mid)
        merge_sort(arr, mid + 1, end)

        merge(arr, begin, mid, end)
        return arr


# Test cases

ll = [5, 2, 4, 6, 1, 3]
first_index = 0
end_index = len(ll) - 1
print(merge_sort(ll, first_index, end_index))

ll2 = [5, 2, 4, 6, 1, 1, 3, 6, 7, 3]
end_index = len(ll2) - 1
print(merge_sort(ll2, 0, len(ll2) - 1))
