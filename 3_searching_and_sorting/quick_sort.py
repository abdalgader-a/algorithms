"""
Description: Implementation of Quick sort algorithm
Input: A sequence of n elements <a1, a2, ..., an>
Output: A permutation <a1', a2', ..., an'> of the input such that
a1'<= a2' <= ... <=an'

Time Complexity: O(n^2) worst case, O(n log(n)) average and best case
Space Complexity: O(1) because it's in-place

"""


def partition(arr, begin, end) -> int:
    pivot = arr[end]
    i = begin - 1
    for j in range(begin, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1


def quick_sort(arr, begin, end):
    if begin < end:
        pivot_idx = partition(arr, begin, end)
        quick_sort(arr, begin, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)
    return arr


# Test cases
ll = [5, 2, 4, 6, 1, 3]
first_index = 0
end_index = len(ll)-1
print(quick_sort(ll, first_index, end_index))

ll2 = [5, 2, 4, 6, 1, 1, 3, 6, 7, 3]
end_index = len(ll2)-1
print(quick_sort(ll2, 0, end_index))

ll3 = [5]
end_index = len(ll3)-1
print(quick_sort(ll3, 0, end_index))
