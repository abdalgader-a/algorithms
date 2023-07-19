"""
Description: Implementation of Selection sort algorithm
Input: A sequence of n elements <a1, a2, ..., an>
Output: A permutation <a1', a2', ..., an'> of the input such that
a1'<= a2' <= ... <=an'

Time Complexity: O(n^2)
Space Complexity: O(1) because it's in-place
"""


def selection_sort(arr) -> list:
    minimum_idx = 0
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] <= arr[minimum_idx]:
                minimum_idx = j
        arr[i], arr[minimum_idx] = arr[minimum_idx], arr[i]
        minimum_idx = i+1

    return arr


# Test cases
ll = [5, 2, 4, 6, 1, 3]
print(selection_sort(ll))

ll2 = [5, 2, 4, 6, 1, 1, 3, 6, 7, 3]
print(selection_sort(ll2))